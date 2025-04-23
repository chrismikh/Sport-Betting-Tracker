import sqlite3
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from pathlib import Path

class BetDatabase:
    def __init__(self, db_path: str = "bets.db"):
        """Initialize the database connection and create tables if they don't exist"""
        self.db_path = db_path
        self.conn = None
        self.cursor = None
        self.connect()
        self.create_tables()
        self.initialize_default_data()

    def connect(self) -> None:
        """Establish connection to the SQLite database"""
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def create_tables(self) -> None:
        """Create the necessary tables if they don't exist"""
        # Create sports_games table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sports_games (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                category TEXT NOT NULL CHECK(category IN ('Sport', 'Esport'))
            )
        ''')

        # Update teams table to reference sport_game_id
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS teams (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sport_game_id INTEGER REFERENCES sports_games(id),
                UNIQUE(name, sport_game_id)
            )
        ''')

        # Update tournaments table to reference sport_game_id
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tournaments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sport_game_id INTEGER REFERENCES sports_games(id),
                UNIQUE(name, sport_game_id)
            )
        ''')

        # Update locations table to reference sport_game_id
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS locations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sport_game_id INTEGER REFERENCES sports_games(id),
                UNIQUE(name, sport_game_id)
            )
        ''')

        # Update bet_types table to reference sport_game_id
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS bet_types (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sport_game_id INTEGER REFERENCES sports_games(id),
                description TEXT,
                UNIQUE(name, sport_game_id)
            )
        ''')

        # Create bet_type_options table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS bet_type_options (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                bet_type_id INTEGER NOT NULL REFERENCES bet_types(id),
                option_type TEXT NOT NULL CHECK(option_type IN ('dropdown', 'text')),
                options TEXT,
                placeholder TEXT
            )
        ''')

        # Update bets table to use sport_game_id instead of sport_game text
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS bets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL CHECK(category IN ('Sport', 'Esport')),
                sport_game_id INTEGER NOT NULL REFERENCES sports_games(id),
                team_a_id INTEGER NOT NULL REFERENCES teams(id),
                team_b_id INTEGER NOT NULL REFERENCES teams(id),
                tournament_id INTEGER REFERENCES tournaments(id),
                location_id INTEGER REFERENCES locations(id),
                bet_type_id INTEGER NOT NULL REFERENCES bet_types(id),
                bet_option TEXT,
                line REAL,
                odds REAL NOT NULL,
                stake REAL NOT NULL,
                result TEXT,
                cash_out_amount REAL,
                date TIMESTAMP NOT NULL
            )
        ''')

        # Create indexes
        self.cursor.execute('CREATE INDEX IF NOT EXISTS idx_sports_games_name ON sports_games(name)')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS idx_teams_name ON teams(name)')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS idx_tournaments_name ON tournaments(name)')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS idx_locations_name ON locations(name)')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS idx_bet_types_name ON bet_types(name)')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS idx_bets_date ON bets(date)')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS idx_bets_category ON bets(category)')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS idx_bets_result ON bets(result)')
        self.conn.commit()

    def initialize_default_data(self) -> None:
        """Initialize default bet types if they don't exist"""
        default_bet_types = [
            ("Match Winner", "Predict the winner of the match"),
            ("Over/Under", "Predict if the total will be over or under a specified line"),
            ("Handicap", "Predict the winner with a handicap applied"),
            ("Correct Score", "Predict the exact final score"),
            ("First Team to Score", "Predict which team will score first"),
            ("Both Teams to Score", "Predict if both teams will score"),
            ("Total Goals", "Predict the total number of goals"),
            ("Half Time/Full Time", "Predict the result at both half time and full time")
        ]

        for name, description in default_bet_types:
            self.cursor.execute(
                'INSERT OR IGNORE INTO bet_types (name, description) VALUES (?, ?)',
                (name, description)
            )
        self.conn.commit()

    def get_or_create_team(self, name: str) -> int:
        """Get team ID or create if it doesn't exist"""
        self.cursor.execute('SELECT id FROM teams WHERE name = ?', (name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        self.cursor.execute('INSERT INTO teams (name) VALUES (?)', (name,))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_or_create_tournament(self, name: str) -> Optional[int]:
        """Get tournament ID or create if it doesn't exist"""
        if not name:
            return None
        self.cursor.execute('SELECT id FROM tournaments WHERE name = ?', (name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        self.cursor.execute('INSERT INTO tournaments (name) VALUES (?)', (name,))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_or_create_location(self, name: str) -> Optional[int]:
        """Get location ID or create if it doesn't exist"""
        if not name:
            return None
        self.cursor.execute('SELECT id FROM locations WHERE name = ?', (name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        self.cursor.execute('INSERT INTO locations (name) VALUES (?)', (name,))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_bet_type_id(self, name: str) -> Optional[int]:
        """Get bet type ID"""
        self.cursor.execute('SELECT id FROM bet_types WHERE name = ?', (name,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def add_bet(self, bet_data: Dict[str, any]) -> int:
        """Add a new bet to the database"""
        try:
            # Get or create IDs for related entities
            sport_game_id = self.get_sport_game_id(bet_data['sport_game'])
            team_a_id = self.get_or_create_team(bet_data['team_a'])
            team_b_id = self.get_or_create_team(bet_data['team_b'])
            tournament_id = self.get_or_create_tournament(bet_data['tournament'])
            location_id = self.get_or_create_location(bet_data['location'])
            bet_type_id = self.get_bet_type_id(bet_data['bet_type'], sport_game_id)

            if not bet_type_id:
                raise ValueError(f"Invalid bet type: {bet_data['bet_type']}")

            query = '''
                INSERT INTO bets (
                    category, sport_game_id, team_a_id, team_b_id, tournament_id,
                    location_id, bet_type_id, bet_option, line, odds, stake,
                    result, cash_out_amount, date
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            values = (
                bet_data['category'],
                sport_game_id,
                team_a_id,
                team_b_id,
                tournament_id,
                location_id,
                bet_type_id,
                bet_data.get('bet_option'),
                bet_data.get('line'),
                bet_data['odds'],
                bet_data['stake'],
                bet_data['result'],
                bet_data.get('cash_out_amount'),
                datetime.now()
            )
            self.cursor.execute(query, values)
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(f"Error adding bet: {e}")
            return -1

    def get_all_bets(self) -> List[Dict[str, any]]:
        """Retrieve all bets from the database with related data"""
        query = '''
            SELECT 
                b.id, b.category, b.sport_game_id, b.odds, b.stake, b.result,
                b.cash_out_amount, b.date, b.bet_option,
                t1.name as team_a, t2.name as team_b,
                tn.name as tournament, l.name as location,
                bt.name as bet_type, bt.description as bet_type_description
            FROM bets b
            LEFT JOIN teams t1 ON b.team_a_id = t1.id
            LEFT JOIN teams t2 ON b.team_b_id = t2.id
            LEFT JOIN tournaments tn ON b.tournament_id = tn.id
            LEFT JOIN locations l ON b.location_id = l.id
            LEFT JOIN bet_types bt ON b.bet_type_id = bt.id
            ORDER BY b.date DESC
        '''
        self.cursor.execute(query)
        columns = [description[0] for description in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_all_teams(self) -> List[Tuple[int, str]]:
        """Get all teams"""
        self.cursor.execute('SELECT id, name FROM teams ORDER BY name')
        return self.cursor.fetchall()

    def get_all_tournaments(self) -> List[Tuple[int, str]]:
        """Get all tournaments"""
        self.cursor.execute('SELECT id, name FROM tournaments ORDER BY name')
        return self.cursor.fetchall()

    def get_all_locations(self) -> List[Tuple[int, str]]:
        """Get all locations"""
        self.cursor.execute('SELECT id, name FROM locations ORDER BY name')
        return self.cursor.fetchall()

    def get_all_bet_types(self) -> List[Tuple[int, str, str]]:
        """Get all bet types"""
        self.cursor.execute('SELECT id, name, description FROM bet_types ORDER BY name')
        return self.cursor.fetchall()

    def close(self) -> None:
        """Close the database connection"""
        if self.conn:
            self.conn.close()

    def __enter__(self):
        """Context manager entry"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()

    # --- Sports/Games ---
    def add_sport_game(self, name: str, category: str) -> int:
        """Add a new sport/game and return its ID"""
        self.cursor.execute('INSERT OR IGNORE INTO sports_games (name, category) VALUES (?, ?)', (name, category))
        self.conn.commit()
        return self.get_sport_game_id(name)

    def get_sport_game_id(self, name: str) -> int:
        """Get sport/game ID by name"""
        self.cursor.execute('SELECT id FROM sports_games WHERE name = ?', (name,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_all_sport_games(self, category: str = None) -> list:
        """Get all sports/games, optionally filtered by category"""
        if category:
            self.cursor.execute('SELECT id, name, category FROM sports_games WHERE category = ? ORDER BY name', (category,))
        else:
            self.cursor.execute('SELECT id, name, category FROM sports_games ORDER BY name')
        return self.cursor.fetchall()

    # --- Bet Types ---
    def add_bet_type(self, name: str, sport_game_id: int, description: str = None) -> int:
        """Add a new bet type for a sport/game and return its ID"""
        self.cursor.execute('INSERT OR IGNORE INTO bet_types (name, sport_game_id, description) VALUES (?, ?, ?)', (name, sport_game_id, description))
        self.conn.commit()
        return self.get_bet_type_id(name, sport_game_id)

    def get_bet_type_id(self, name: str, sport_game_id: int) -> int:
        """Get bet type ID by name and sport_game_id"""
        self.cursor.execute('SELECT id FROM bet_types WHERE name = ? AND sport_game_id = ?', (name, sport_game_id))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_bet_types_for_sport_game(self, sport_game_id: int) -> list:
        """Get all bet types for a sport/game"""
        self.cursor.execute('SELECT id, name, description FROM bet_types WHERE sport_game_id = ? ORDER BY name', (sport_game_id,))
        return self.cursor.fetchall()

    # --- Bet Type Options ---
    def add_bet_type_option(self, bet_type_id: int, option_type: str, options: str = None, placeholder: str = None) -> int:
        """Add bet type option (dropdown/text) for a bet type"""
        self.cursor.execute('INSERT INTO bet_type_options (bet_type_id, option_type, options, placeholder) VALUES (?, ?, ?, ?)', (bet_type_id, option_type, options, placeholder))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_bet_type_options(self, bet_type_id: int) -> list:
        """Get all options for a bet type"""
        self.cursor.execute('SELECT id, option_type, options, placeholder FROM bet_type_options WHERE bet_type_id = ?', (bet_type_id,))
        return self.cursor.fetchall()

    # --- Teams ---
    def add_team(self, name: str, sport_game_id: int) -> int:
        """Add a new team for a sport/game and return its ID"""
        self.cursor.execute('INSERT OR IGNORE INTO teams (name, sport_game_id) VALUES (?, ?)', (name, sport_game_id))
        self.conn.commit()
        self.cursor.execute('SELECT id FROM teams WHERE name = ? AND sport_game_id = ?', (name, sport_game_id))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_teams_for_sport_game(self, sport_game_id: int) -> list:
        """Get all teams for a sport/game"""
        self.cursor.execute('SELECT id, name FROM teams WHERE sport_game_id = ? ORDER BY name', (sport_game_id,))
        return self.cursor.fetchall()

    # --- Tournaments ---
    def add_tournament(self, name: str, sport_game_id: int) -> int:
        """Add a new tournament for a sport/game and return its ID"""
        self.cursor.execute('INSERT OR IGNORE INTO tournaments (name, sport_game_id) VALUES (?, ?)', (name, sport_game_id))
        self.conn.commit()
        self.cursor.execute('SELECT id FROM tournaments WHERE name = ? AND sport_game_id = ?', (name, sport_game_id))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_tournaments_for_sport_game(self, sport_game_id: int) -> list:
        """Get all tournaments for a sport/game"""
        self.cursor.execute('SELECT id, name FROM tournaments WHERE sport_game_id = ? ORDER BY name', (sport_game_id,))
        return self.cursor.fetchall()

    # --- Locations ---
    def add_location(self, name: str, sport_game_id: int) -> int:
        """Add a new location for a sport/game and return its ID"""
        self.cursor.execute('INSERT OR IGNORE INTO locations (name, sport_game_id) VALUES (?, ?)', (name, sport_game_id))
        self.conn.commit()
        self.cursor.execute('SELECT id FROM locations WHERE name = ? AND sport_game_id = ?', (name, sport_game_id))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_locations_for_sport_game(self, sport_game_id: int) -> list:
        """Get all locations for a sport/game"""
        self.cursor.execute('SELECT id, name FROM locations WHERE sport_game_id = ? ORDER BY name', (sport_game_id,))
        return self.cursor.fetchall() 