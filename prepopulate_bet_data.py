from database.bet_database import BetDatabase
import json

# --- Comprehensive Sports and Esports Data ---

SPORTS = [
    {
        'name': 'Football',
        'category': 'Sport',
        'bet_types': [
            {'name': 'Match Result (1X2)', 'type': 'dropdown', 'options': ['Team A', 'Draw', 'Team B']},
            {'name': 'Double Chance', 'type': 'dropdown', 'options': ['Team A or Draw', 'Team A or Team B', 'Draw or Team B']},
            {'name': 'Draw No Bet', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Match Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Asian Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'European Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Over/Under Goals', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Both Teams to Score', 'type': 'dropdown', 'options': ['Yes', 'No']},
            {'name': 'Correct Score', 'type': 'text', 'placeholder': 'Enter score (e.g., 2-1)'},
            {'name': 'Half-Time/Full-Time Result', 'type': 'dropdown', 'options': [
                'Team A/Team A', 'Team A/Draw', 'Team A/Team B',
                'Draw/Team A', 'Draw/Draw', 'Draw/Team B',
                'Team B/Team A', 'Team B/Draw', 'Team B/Team B']},
            {'name': 'Total Corners', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Total Cards', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'First Team to Score', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'No Goal']},
            {'name': 'Winning Margin', 'type': 'dropdown', 'options': ['1 Goal', '2 Goals', '3+ Goals', 'Draw']},
            {'name': 'Exact Scoreline', 'type': 'text', 'placeholder': 'Enter exact scoreline'},
            {'name': 'Team to Win Both Halves', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Neither']},
            {'name': 'Team to Score in Both Halves', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Neither']},
            {'name': 'Half-Time Winner', 'type': 'dropdown', 'options': ['Team A', 'Draw', 'Team B']},
            {'name': 'Half-Time Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Half-Time Total Goals (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Team A Total Goals (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Team B Total Goals (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
        ],
        'teams': [
            'Manchester United', 'Liverpool', 'Barcelona', 'Real Madrid', 'Bayern Munich', 'PSG', 'Juventus', 'Arsenal'
        ],
        'locations': [
            'Wembley Stadium', 'Camp Nou', 'Santiago Bernabeu', 'Allianz Arena'
        ],
        'tournaments': [
            'Premier League', 'La Liga', 'Champions League', 'World Cup'
        ]
    },
    {
        'name': 'American Football',
        'category': 'Sport',
        'bet_types': [
            {'name': 'Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Match Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Total Points (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'First/Second Half Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': 'Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': 'Total Touchdowns', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Race to X Points', 'type': 'text', 'placeholder': 'Enter X'},
            {'name': 'Team Totals', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Player Props', 'type': 'text', 'placeholder': 'Describe player prop'},
            {'name': '1st Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '2nd Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '3rd Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '4th Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '1st Quarter Total Points (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '2nd Quarter Total Points (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '3rd Quarter Total Points (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '4th Quarter Total Points (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Total Points (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Team A Total Points (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'First/Second Half Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': 'Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': 'Race to X Points', 'type': 'text', 'placeholder': 'Enter X'},
            {'name': 'Winning Margin', 'type': 'dropdown', 'options': ['1-5', '6-10', '11-15', '16+']},
            {'name': 'Team Totals', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Player Props', 'type': 'text', 'placeholder': 'Describe player prop'},
            {'name': '1st Inning Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '2nd Inning Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '3rd Inning Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '1st Inning Total Runs (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '2nd Inning Total Runs (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '3rd Inning Total Runs (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
        ],
        'teams': [
            'New England Patriots', 'Dallas Cowboys', 'Green Bay Packers', 'Alabama Crimson Tide'
        ],
        'locations': [
            'Lambeau Field', 'AT&T Stadium', 'Rose Bowl'
        ],
        'tournaments': [
            'NFL', 'NCAA', 'Super Bowl'
        ]
    },
    {
        'name': 'Basketball',
        'category': 'Sport',
        'bet_types': [
            {'name': 'Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': '1st Quarter Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': '2nd Quarter Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': '3rd Quarter Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': '4th Quarter Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': '1st Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '2nd Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '3rd Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '4th Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '1st Quarter Total Points (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '2nd Quarter Total Points (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '3rd Quarter Total Points (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '4th Quarter Total Points (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Total Points (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Team A Total Points (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'First/Second Half Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': 'Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': 'Race to X Points', 'type': 'text', 'placeholder': 'Enter X'},
            {'name': 'Winning Margin', 'type': 'dropdown', 'options': ['1-5', '6-10', '11-15', '16+']},
            {'name': 'Team Totals', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Player Props', 'type': 'text', 'placeholder': 'Describe player prop'},
            {'name': '1st Inning Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '2nd Inning Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '3rd Inning Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '1st Inning Total Runs (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '2nd Inning Total Runs (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '3rd Inning Total Runs (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
        ],
        'teams': [
            'LA Lakers', 'Chicago Bulls', 'Boston Celtics', 'Golden State Warriors', 'Miami Heat'
        ],
        'locations': [
            'Madison Square Garden', 'Staples Center', 'TD Garden'
        ],
        'tournaments': [
            'NBA', 'EuroLeague', 'Olympics'
        ]
    },
    {
        'name': 'Baseball',
        'category': 'Sport',
        'bet_types': [
            {'name': 'Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Run Line Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Total Runs (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'First 5 Innings Result', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': 'Team Totals', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Player Props', 'type': 'text', 'placeholder': 'Describe player prop'},
            {'name': '1st Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '2nd Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '3rd Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '4th Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '1st Quarter Total Runs (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '2nd Quarter Total Runs (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '3rd Quarter Total Runs (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '4th Quarter Total Runs (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Total Runs (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Team A Total Runs (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Team B Total Runs (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '1st Inning Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '2nd Inning Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '3rd Inning Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '1st Inning Total Runs (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '2nd Inning Total Runs (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '3rd Inning Total Runs (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Second Period Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': 'Third Period Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': 'First Period Total Goals (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Second Period Total Goals (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Third Period Total Goals (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
        ],
        'teams': [
            'New York Yankees', 'Los Angeles Dodgers', 'Boston Red Sox', 'Yomiuri Giants'
        ],
        'locations': [
            'Yankee Stadium', 'Dodger Stadium', 'Fenway Park'
        ],
        'tournaments': [
            'MLB', 'NPB', 'World Series'
        ]
    },
    {
        'name': 'Ice Hockey',
        'category': 'Sport',
        'bet_types': [
            {'name': 'Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Match Result (1x2)', 'type': 'dropdown', 'options': ['Team A', 'Draw', 'Team B']},
            {'name': 'Double Chance', 'type': 'dropdown', 'options': ['Team A or Draw', 'Draw or Team B', 'Team A or Team B']},
            {'name': 'Total Goals (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'First Period Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': 'Team to Score First', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Winning Margin', 'type': 'dropdown', 'options': ['1 Goal', '2 Goals', '3+ Goals', 'Draw']},
            {'name': 'Player Props', 'type': 'text', 'placeholder': 'Describe player prop'},
            {'name': '1st Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '2nd Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '3rd Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '4th Quarter Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B', 'Draw']},
            {'name': '1st Quarter Total Goals (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '2nd Quarter Total Goals (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '3rd Quarter Total Goals (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': '4th Quarter Total Goals (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Total Goals (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Team A Total Goals (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Team B Total Goals (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
        ],
        'teams': [
            'Montreal Canadiens', 'Toronto Maple Leafs', 'Boston Bruins', 'Jokerit'
        ],
        'locations': [
            'Bell Centre', 'United Center', 'Hartwall Arena'
        ],
        'tournaments': [
            'NHL', 'Liiga', 'Stanley Cup'
        ]
    },
    {
        'name': 'Tennis',
        'category': 'Sport',
        'bet_types': [
            {'name': 'Match Winner', 'type': 'dropdown', 'options': ['Player A', 'Player B']},
            {'name': 'Set Betting', 'type': 'text', 'placeholder': 'Enter set score (e.g., 2-1)'},
            {'name': 'Total Games (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Handicap Games (Match Handicap)', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'First Set Winner', 'type': 'dropdown', 'options': ['Player A', 'Player B']},
            {'name': 'Player to Win a Set', 'type': 'dropdown', 'options': ['Player A', 'Player B']},
            {'name': 'Tie-Break in Match (Yes/No)', 'type': 'dropdown', 'options': ['Yes', 'No']},
            {'name': 'Total Aces', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Total Double Faults', 'type': 'dropdown', 'options': ['Over', 'Under']},
        ],
        'teams': [
            'Novak Djokovic', 'Rafael Nadal', 'Serena Williams', 'Iga Swiatek'
        ],
        'locations': [
            'Wimbledon', 'Roland Garros', 'Arthur Ashe Stadium'
        ],
        'tournaments': [
            'ATP', 'WTA', 'US Open', 'Australian Open'
        ]
    },
    {
        'name': 'Boxing',
        'category': 'Sport',
        'bet_types': [
            {'name': 'Fight Winner', 'type': 'dropdown', 'options': ['Boxer A', 'Boxer B']},
            {'name': 'Method of Victory', 'type': 'dropdown', 'options': ['KO/TKO', 'Decision', 'Draw']},
            {'name': 'Round Betting', 'type': 'text', 'placeholder': 'Enter round (e.g., Round 1, Round 2)'},
            {'name': 'Total Rounds (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Will the Fight Go the Distance', 'type': 'dropdown', 'options': ['Yes', 'No']},
            {'name': 'Draw', 'type': 'dropdown', 'options': ['Yes', 'No']},
        ],
        'teams': [
            'Tyson Fury', 'Canelo Alvarez', 'Anthony Joshua', 'Deontay Wilder'
        ],
        'locations': [
            'Madison Square Garden', 'T-Mobile Arena', 'O2 Arena'
        ],
        'tournaments': [
            'WBC', 'WBA', 'IBF', 'WBO'
        ]
    },
    {
        'name': 'MMA',
        'category': 'Sport',
        'bet_types': [
            {'name': 'Fight Winner', 'type': 'dropdown', 'options': ['Fighter A', 'Fighter B']},
            {'name': 'Method of Victory', 'type': 'dropdown', 'options': ['KO/TKO', 'Submission', 'Decision', 'Draw']},
            {'name': 'Round Betting', 'type': 'text', 'placeholder': 'Enter round (e.g., Round 1, Round 2)'},
            {'name': 'Total Rounds (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Will the Fight Go the Distance', 'type': 'dropdown', 'options': ['Yes', 'No']},
            {'name': 'Draw', 'type': 'dropdown', 'options': ['Yes', 'No']},
        ],
        'teams': [
            'Conor McGregor', 'Khabib Nurmagomedov', 'Israel Adesanya', 'Amanda Nunes'
        ],
        'locations': [
            'Madison Square Garden', 'T-Mobile Arena', 'O2 Arena'
        ],
        'tournaments': [
            'UFC', 'Bellator', 'ONE Championship', 'PFL'
        ]
    },
]

ESPORTS = [
    {
        'name': 'Counter-Strike 2',
        'category': 'Esport',
        'bet_types': [
            {'name': 'Match Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Match Winner (1x2)', 'type': 'dropdown', 'options': ['Team A', 'Draw', 'Team B']},
            {'name': 'Map Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Map Winner (1x2)', 'type': 'dropdown', 'options': ['Team A', 'Draw', 'Team B']},
            {'name': 'Correct Map Score', 'type': 'text', 'placeholder': 'Enter map score (e.g., 2-1)'},
            {'name': 'Total Maps (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Match Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Map Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': '1st Pistol Round Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': '2nd Pistol Round Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
        ],
        'teams': [
            'Natus Vincere', 'FaZe', 'G2', 'Vitality', 'Spirit', 'MOUZ', 'Aurora', 'The MongolZ', 'Falcons', 'Virtus.pro',
            '3DMAX', 'GamerLegion', 'Liquid', 'Complexity', 'Astralis', 'FURIA', 'paiN', 'SAW', 'M80', 'MIBR', 'TYLOO', 'HEROIC', 'Apogee',
            'BIG', 'BetBoom', 'FlyQuest', 'Nemiga', 'OG', 'Wildcard', 'Rare Atom', 'Legacy', 'B8'
        ],
        'locations': [
            'Dust II', 'Mirage', 'Inferno', 'Nuke', 'Vertigo', 'Overpass', 'Anubis', 'Ancient', 'Train'
        ],
        'tournaments': [
            'ESL Pro League', 'BLAST Premier', 'IEM Katowice'
        ]
    },
    {
        'name': 'Dota 2',
        'category': 'Esport',
        'bet_types': [
            {'name': 'Match Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Map Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Correct Map Score', 'type': 'text', 'placeholder': 'Enter map score (e.g., 2-1)'},
            {'name': 'Total Maps (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Match Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Map Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
        ],
        'teams': [
            'OG', 'Team Secret', 'Evil Geniuses', 'PSG.LGD'
        ],
        'locations': [
            'The International Arena', 'ESL One Arena'
        ],
        'tournaments': [
            'The International', 'ESL One', 'DPC Major'
        ]
    },
    {
        'name': 'League of Legends',
        'category': 'Esport',
        'bet_types': [
            {'name': 'Match Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Map Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Correct Map Score', 'type': 'text', 'placeholder': 'Enter map score (e.g., 2-1)'},
            {'name': 'Total Maps (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Match Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Map Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
        ],
        'teams': [
            'T1', 'G2 Esports', 'Fnatic', 'Cloud9'
        ],
        'locations': [
            "Summoner's Rift", 'Worlds Arena'
        ],
        'tournaments': [
            'Worlds', 'MSI', 'LEC', 'LCS'
        ]
    },
    {
        'name': 'Valorant',
        'category': 'Esport',
        'bet_types': [
            {'name': 'Match Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Match Winner (1x2)', 'type': 'dropdown', 'options': ['Team A', 'Draw', 'Team B']},
            {'name': 'Map Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Map Winner (1x2)', 'type': 'dropdown', 'options': ['Team A', 'Draw', 'Team B']},
            {'name': 'Correct Map Score', 'type': 'text', 'placeholder': 'Enter map score (e.g., 2-1)'},
            {'name': 'Total Rounds (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Match Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Map Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': '1st Pistol Round Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': '2nd Pistol Round Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
        ],
        'teams': [
            'Sentinels', 'Fnatic', 'Team Liquid', '100 Thieves'
        ],
        'locations': [
            'Bind', 'Haven', 'Split', 'Ascent'
        ],
        'tournaments': [
            'VCT', 'Champions Tour', 'Masters'
        ]
    },
    {
        'name': 'Overwatch',
        'category': 'Esport',
        'bet_types': [
            {'name': 'Match Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Match Winner (1x2)', 'type': 'dropdown', 'options': ['Team A', 'Draw', 'Team B']},
            {'name': 'Map Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Map Winner (1x2)', 'type': 'dropdown', 'options': ['Team A', 'Draw', 'Team B']},
            {'name': 'Correct Map Score', 'type': 'text', 'placeholder': 'Enter map score (e.g., 3-2)'},
            {'name': 'Total Rounds/Maps (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Match Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Map Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
        ],
        'teams': [
            'Dallas Fuel', 'San Francisco Shock', 'Seoul Dynasty', 'Shanghai Dragons'
        ],
        'locations': [
            'Blizzard Arena', 'Seoul Arena'
        ],
        'tournaments': [
            'Overwatch League', 'OWL Playoffs'
        ]
    },
    {
        'name': 'Call of Duty',
        'category': 'Esport',
        'bet_types': [
            {'name': 'Match Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Match Winner (1x2)', 'type': 'dropdown', 'options': ['Team A', 'Draw', 'Team B']},
            {'name': 'Map Winner', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Map Winner (1x2)', 'type': 'dropdown', 'options': ['Team A', 'Draw', 'Team B']},
            {'name': 'Correct Map Score', 'type': 'text', 'placeholder': 'Enter map score (e.g., 3-2)'},
            {'name': 'Total Maps/Rounds (Over/Under)', 'type': 'dropdown', 'options': ['Over', 'Under']},
            {'name': 'Match Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
            {'name': 'Map Handicap', 'type': 'dropdown', 'options': ['Team A', 'Team B']},
        ],
        'teams': [
            'OpTic Gaming', 'Atlanta FaZe', 'LA Thieves', 'Toronto Ultra'
        ],
        'locations': [
            'Call of Duty League Arena', 'Esports Stadium Arlington'
        ],
        'tournaments': [
            'Call of Duty League', 'CDL Playoffs'
        ]
    },
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