from database.bet_database import BetDatabase
import json

# --- Comprehensive Sports and Esports Data ---

SPORTS = [
    {
        'name': 'Football',
        'category': 'Sport',
        'bet_types': [
            {'name': 'Match Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '1X2', 'type': 'dropdown', 'options': ['Team A', 'Draw', 'Team B']},
            {'name': 'Double Chance', 'type': 'dropdown', 'options': ['Team A or Draw', 'Team A or Team B', 'Draw or Team B']},
            {'name': 'Total Goals', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Both Teams to Score', 'type': 'dropdown', 'options': ['Yes', 'No']},
            {'name': 'Correct Score', 'type': 'text', 'placeholder': 'Enter score (e.g., 2-1)'},
            {'name': 'Half Time/Full Time', 'type': 'dropdown', 'options': [
                'Team A/Team A', 'Team A/Draw', 'Team A/Team B',
                'Draw/Team A', 'Draw/Draw', 'Draw/Team B',
                'Team B/Team A', 'Team B/Draw', 'Team B/Team B']},
        ],
        'teams': [
            'Manchester United', 'Liverpool', 'Barcelona', 'Real Madrid',
            'Bayern Munich', 'PSG', 'Juventus', 'Arsenal', 'Chelsea',
            'Manchester City', 'Tottenham Hotspur'
        ],
        'locations': [
            'Wembley Stadium', 'Camp Nou', 'Santiago Bernabeu', 'Allianz Arena',
            'San Siro', 'Parc des Princes', 'Old Trafford'
        ],
        'tournaments': [
            'Premier League', 'La Liga', 'Bundesliga', 'Serie A', 'Ligue 1',
            'Champions League', 'Europa League', 'World Cup', 'Euro Cup'
        ]
    },
    {
        'name': 'Basketball',
        'category': 'Sport',
        'bet_types': [
            {'name': 'Winner (incl. Overtime)', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Double Chance', 'type': 'dropdown', 'options': ['Team A or Team B']},
            {'name': 'Total Points', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Correct Score', 'type': 'text', 'placeholder': 'Enter score (e.g., 100-98)'},
        ],
        'teams': [
            'LA Lakers', 'Chicago Bulls', 'Boston Celtics', 'Golden State Warriors'
        ],
        'locations': [
            'Madison Square Garden', 'Staples Center', 'TD Garden', 'United Center'
        ],
        'tournaments': [
            'NBA', 'EuroLeague', 'FIBA World Cup', 'Olympics'
        ]
    },
    {
        'name': 'Ice Hockey',
        'category': 'Sport',
        'bet_types': [
            {'name': 'Match Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': 'Total Goals', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'First Team to Score', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
        ],
        'teams': [
            'Montreal Canadiens', 'Toronto Maple Leafs', 'Boston Bruins', 'Chicago Blackhawks'
        ],
        'locations': [
            'Madison Square Garden', 'Bell Centre', 'United Center', 'Rogers Arena'
        ],
        'tournaments': [
            'NHL', 'Stanley Cup', 'World Championship', 'Olympics'
        ]
    },
    # Add more sports as needed...
]

ESPORTS = [
    {
        'name': 'Counter-Strike 2',
        'category': 'Esport',
        'bet_types': [
            {'name': 'Match Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Map Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Total Rounds', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'First Blood', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Team to Win Pistol Round', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
        ],
        'teams': [
            'Astralis', 'Natus Vincere', 'FaZe Clan', 'Team Liquid', 'Vitality'
        ],
        'locations': [
            'Dust II', 'Mirage', 'Inferno', 'Nuke', 'Overpass', 'Vertigo'
        ],
        'tournaments': [
            'Major Championships', 'ESL Pro League', 'BLAST Premier', 'IEM'
        ]
    },
    {
        'name': 'League of Legends',
        'category': 'Esport',
        'bet_types': [
            {'name': 'Match Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Map Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'First Blood', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'First Tower', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Total Kills', 'type': 'dropdown', 'options': ['Over', 'Under']},
        ],
        'teams': [
            'Fnatic', 'G2 Esports', 'T1', 'Cloud9', 'Team Liquid'
        ],
        'locations': [
            "Summoner's Rift", 'Howling Abyss'
        ],
        'tournaments': [
            'Worlds', 'MSI', 'LEC', 'LCS', 'LCK', 'LPL'
        ]
    },
    {
        'name': 'Valorant',
        'category': 'Esport',
        'bet_types': [
            {'name': 'Match Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Map Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Total Rounds', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'First Blood', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Team to Win Pistol Round', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
        ],
        'teams': [
            'Sentinels', 'Fnatic', 'Team Liquid', 'G2 Esports', '100 Thieves', 'Cloud9', 'NRG', 'TSM'
        ],
        'locations': [
            'Bind', 'Haven', 'Split', 'Ascent', 'Icebox', 'Breeze', 'Fracture'
        ],
        'tournaments': [
            'VCT', 'Champions Tour', 'Masters', 'Champions'
        ]
    },
    # Add more esports as needed...
]

def prepopulate():
    with BetDatabase() as db:
        for sport in SPORTS + ESPORTS:
            sport_game_id = db.add_sport_game(sport['name'], sport['category'])
            # Bet types
            for bt in sport['bet_types']:
                bet_type_id = db.add_bet_type(bt['name'], sport_game_id, "")
                if bt['type'] == 'dropdown':
                    db.add_bet_type_option(bet_type_id, 'dropdown', options=json.dumps(bt['options']), placeholder=None)
                elif bt['type'] == 'text':
                    db.add_bet_type_option(bet_type_id, 'text', options=None, placeholder=bt.get('placeholder', 'Enter bet option'))
            # Teams
            for team in sport.get('teams', []):
                db.add_team(team, sport_game_id)
            # Locations
            for location in sport.get('locations', []):
                db.add_location(location, sport_game_id)
            # Tournaments
            for tournament in sport.get('tournaments', []):
                db.add_tournament(tournament, sport_game_id)
    print("Prepopulation complete!")

if __name__ == "__main__":
    prepopulate() 