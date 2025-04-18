from typing import Dict, List, Tuple

class BetData:
    """Class containing all static bet data"""
    
    # Category to location mapping
    CATEGORY_LOCATIONS = {
        "Sport": "Stadium/City:",
        "Esport": "Map:"
    }
    
    # Sport and Esport options
    SPORT_OPTIONS = [
        "Football", "Basketball", "Tennis", "Baseball", "Ice Hockey",
        "Cricket", "Rugby", "Golf", "Boxing", "MMA"
    ]
    
    ESPORT_OPTIONS = [
        "League of Legends", "Dota 2", "Counter-Strike 2", "Valorant",
        "Overwatch", "Rocket League", "Fortnite", "Apex Legends",
        "Starcraft", "Hearthstone"
    ]

    # Bet type mappings for different sports and games
    BET_TYPE_MAPPINGS = {
        # Sports
        "Football": [
            ("Match Winner", "Predict the winner of the match"),
            ("Total Goals", "Predict if total goals will be over/under a certain number"),
            ("Both Teams to Score", "Predict if both teams will score"),
            ("Correct Score", "Predict the exact final score"),
        ],
        "Basketball": [
            ("Match Winner", "Predict the winner of the match"),
            ("Total Points", "Predict if total points will be over/under a certain number"),
        ],
        "Tennis": [
            ("Match Winner", "Predict the winner of the match"),
            ("Total Sets", "Predict if total sets will be over/under a certain number"),
        ],
        "Baseball": [
            ("Match Winner", "Predict the winner of the match"),
        ],
        "Ice Hockey": [
            ("Match Winner", "Predict the winner of the match"),
            ("Total Goals", "Predict if total goals will be over/under a certain number"),
            ("First Team to Score", "Predict which team will score first"),
        ],
        "Cricket": [
            ("Match Winner", "Predict the winner of the match"),
            ("Total Runs", "Predict if total runs will be over/under a certain number"),
            ("First Team to Score", "Predict which team will score first"),
        ],
        "Rugby": [
            ("Match Winner", "Predict the winner of the match"),
            ("Total Points", "Predict if total points will be over/under a certain number"),
            ("First Team to Score", "Predict which team will score first"),
        ],
        "Golf": [
            ("Tournament Winner", "Predict the winner of the tournament"),
            ("Top 5 Finish", "Predict if a player will finish in the top 5"),
            ("Match Bet", "Predict which player will have a better score"),
        ],
        "Boxing": [
            ("Match Winner", "Predict the winner of the match"),
            ("Method of Victory", "Predict how the match will end"),
            ("Round Betting", "Predict which round the match will end"),
            ("Total Rounds", "Predict if total rounds will be over/under a certain number")
        ],
        "MMA": [
            ("Match Winner", "Predict the winner of the match"),
            ("Method of Victory", "Predict how the match will end"),
            ("Round Betting", "Predict which round the match will end"),
            ("Total Rounds", "Predict if total rounds will be over/under a certain number")
        ],
        # Esports
        "League of Legends": [
            ("Match Winner", "Predict the winner of the match"),
            ("Map Winner", "Predict the winner of a specific map"),
            ("First Blood", "Predict which team gets the first kill"),
            ("First Tower", "Predict which team destroys the first tower"),
            ("Total Kills", "Predict if total kills will be over/under a certain number")
        ],
        "Dota 2": [
            ("Match Winner", "Predict the winner of the match"),
            ("Map Winner", "Predict the winner of a specific map"),
            ("First Blood", "Predict which team gets the first kill"),
            ("First Tower", "Predict which team destroys the first tower"),
            ("Total Kills", "Predict if total kills will be over/under a certain number")
        ],
        "Counter-Strike 2": [
            ("Match Winner", "Predict the winner of the match"),
            ("Map Winner", "Predict the winner of a specific map"),
            ("Total Rounds", "Predict if total rounds will be over/under a certain number"),
            ("First Blood", "Predict which team gets the first kill"),
            ("Team to Win Pistol Round", "Predict which team wins the pistol round")
        ],
        "Valorant": [
            ("Match Winner", "Predict the winner of the match"),
            ("Map Winner", "Predict the winner of a specific map"),
            ("Total Rounds", "Predict if total rounds will be over/under a certain number"),
            ("First Blood", "Predict which team gets the first kill"),
            ("Team to Win Pistol Round", "Predict which team wins the pistol round")
        ],
        "Overwatch": [
            ("Match Winner", "Predict the winner of the match"),
            ("Map Winner", "Predict the winner of a specific map"),
            ("Total Rounds", "Predict if total rounds will be over/under a certain number"),
        ],
        "Rocket League": [
            ("Match Winner", "Predict the winner of the match"),
            ("Game Winner", "Predict the winner of a specific game"),
            ("Total Goals", "Predict if total goals will be over/under a certain number"),
            ("First Team to Score", "Predict which team scores first"),
        ],
        "Fortnite": [
            ("Match Winner", "Predict the winner of the match"),
            ("Top 3 Finish", "Predict if a player will finish in the top 3"),
            ("Total Kills", "Predict if total kills will be over/under a certain number"),
            ("First Kill", "Predict which player gets the first kill"),
        ],
        "Apex Legends": [
            ("Match Winner", "Predict the winner of the match"),
            ("Top 3 Finish", "Predict if a team will finish in the top 3"),
            ("Total Kills", "Predict if total kills will be over/under a certain number"),
            ("First Kill", "Predict which team gets the first kill"),
        ],
        "Starcraft": [
            ("Match Winner", "Predict the winner of the match"),
            ("Map Winner", "Predict the winner of a specific map"),
            ("First to Reach Supply", "Predict which player reaches a certain supply first"),
            ("Total Games", "Predict if total games will be over/under a certain number"),
        ],
        "Hearthstone": [
            ("Match Winner", "Predict the winner of the match"),
            ("Game Winner", "Predict the winner of a specific game"),
            ("First to Win Game", "Predict which player wins the first game"),
            ("Total Games", "Predict if total games will be over/under a certain number"),
        ]
    }

    # Common tournaments for each sport/game
    TOURNAMENTS = {
        # Sports
        "Football": [
            "Premier League", "La Liga", "Bundesliga", "Serie A", "Ligue 1",
            "Champions League", "Europa League", "World Cup", "Euro Cup"
        ],
        "Basketball": [
            "NBA", "EuroLeague", "FIBA World Cup", "Olympics"
        ],
        "Tennis": [
            "Grand Slams", "ATP Tour", "WTA Tour", "Davis Cup", "Fed Cup"
        ],
        "Baseball": [
            "MLB", "World Series", "All-Star Game", "Playoffs"
        ],
        "Ice Hockey": [
            "NHL", "Stanley Cup", "World Championship", "Olympics"
        ],
        "Cricket": [
            "ICC World Cup", "T20 World Cup", "Ashes", "IPL", "Big Bash League"
        ],
        "Rugby": [
            "Six Nations", "Rugby World Cup", "Super Rugby", "Premiership"
        ],
        "Golf": [
            "Masters", "US Open", "British Open", "PGA Championship", "Ryder Cup"
        ],
        "Boxing": [
            "World Championship", "Regional Championship", "Title Fight", "Exhibition"
        ],
        "MMA": [
            "UFC", "Bellator", "ONE Championship", "PFL", "Regional Championship"
        ],
        # Esports
        "League of Legends": [
            "Worlds", "MSI", "LEC", "LCS", "LCK", "LPL"
        ],
        "Dota 2": [
            "The International", "Major Championships", "DPC", "Regional Leagues"
        ],
        "Counter-Strike 2": [
            "Major Championships", "ESL Pro League", "BLAST Premier", "IEM"
        ],
        "Valorant": [
            "VCT", "Champions Tour", "Masters", "Champions"
        ],
        "Overwatch": [
            "Overwatch League", "World Cup", "Contenders", "Regional Tournaments"
        ],
        "Rocket League": [
            "RLCS", "World Championship", "Regional Championships", "Majors"
        ],
        "Fortnite": [
            "World Cup", "FNCS", "Cash Cups", "DreamHack"
        ],
        "Apex Legends": [
            "ALGS", "Championship", "Pro League", "Regional Series"
        ],
        "Starcraft": [
            "GSL", "ASL", "WCS", "IEM", "DreamHack"
        ],
        "Hearthstone": [
            "World Championship", "Masters Tour", "Grandmasters", "Regional Qualifiers"
        ]
    }

    # Common locations for each sport/game
    LOCATIONS = {
        # Sports
        "Football": [
            "Wembley Stadium", "Camp Nou", "Santiago Bernabeu", "Allianz Arena",
            "San Siro", "Parc des Princes", "Old Trafford"
        ],
        "Basketball": [
            "Madison Square Garden", "Staples Center", "TD Garden", "United Center"
        ],
        "Tennis": [
            "Wimbledon", "Roland Garros", "US Open", "Australian Open"
        ],
        "Baseball": [
            "Yankee Stadium", "Fenway Park", "Wrigley Field", "Dodger Stadium"
        ],
        "Ice Hockey": [
            "Madison Square Garden", "Bell Centre", "United Center", "Rogers Arena"
        ],
        "Cricket": [
            "Lord's", "MCG", "Eden Gardens", "Wanderers Stadium"
        ],
        "Rugby": [
            "Twickenham", "Millennium Stadium", "Stade de France", "Eden Park"
        ],
        "Golf": [
            "Augusta National", "St. Andrews", "Pebble Beach", "Pinehurst"
        ],
        "Boxing": [
            "Madison Square Garden", "MGM Grand", "T-Mobile Arena", "O2 Arena"
        ],
        "MMA": [
            "T-Mobile Arena", "Madison Square Garden", "O2 Arena", "Etihad Arena"
        ],
        # Esports
        "League of Legends": [
            "Summoner's Rift", "Howling Abyss"
        ],
        "Dota 2": [
            "Radiant", "Dire"
        ],
        "Counter-Strike 2": [
            "Dust II", "Mirage", "Inferno", "Nuke", "Overpass", "Vertigo"
        ],
        "Valorant": [
            "Bind", "Haven", "Split", "Ascent", "Icebox", "Breeze", "Fracture"
        ],
        "Overwatch": [
            "King's Row", "Hanamura", "Temple of Anubis", "Volskaya Industries"
        ],
        "Rocket League": [
            "DFH Stadium", "Mannfield", "Champions Field", "Urban Central"
        ],
        "Fortnite": [
            "Battle Royale Island", "Creative Island", "Party Royale"
        ],
        "Apex Legends": [
            "World's Edge", "Olympus", "Storm Point", "Kings Canyon"
        ],
        "Starcraft": [
            "Lost Temple", "Jade", "Neo Human", "Neo Zerg"
        ],
        "Hearthstone": [
            "Tavern", "Arena", "Battlegrounds"
        ]
    }

    # Common teams for each sport/game
    TEAMS = {
        # Sports
        "Football": [
            "Manchester United", "Liverpool", "Barcelona", "Real Madrid",
            "Bayern Munich", "PSG", "Juventus", "Arsenal", "Chelsea",
            "Manchester City", "Tottenham Hotspur"
        ],
        "Basketball": [
            "LA Lakers", "Chicago Bulls", "Boston Celtics", "Golden State Warriors"
        ],
        "Tennis": [
            "Novak Djokovic", "Rafael Nadal", "Roger Federer", "Serena Williams"
        ],
        "Baseball": [
            "New York Yankees", "Boston Red Sox", "Los Angeles Dodgers", "Chicago Cubs"
        ],
        "Ice Hockey": [
            "Montreal Canadiens", "Toronto Maple Leafs", "Boston Bruins", "Chicago Blackhawks"
        ],
        "Cricket": [
            "India", "Australia", "England", "South Africa", "Pakistan"
        ],
        "Rugby": [
            "New Zealand", "South Africa", "England", "Australia", "Ireland"
        ],
        "Golf": [
            "Tiger Woods", "Rory McIlroy", "Jon Rahm", "Dustin Johnson"
        ],
        "Boxing": [
            "Canelo Alvarez", "Tyson Fury", "Anthony Joshua", "Oleksandr Usyk"
        ],
        "MMA": [
            "Israel Adesanya", "Kamaru Usman", "Alexander Volkanovski", "Charles Oliveira"
        ],
        # Esports
        "League of Legends": [
            "Fnatic", "G2 Esports", "T1", "Cloud9", "Team Liquid"
        ],
        "Dota 2": [
            "OG", "Team Secret", "PSG.LGD", "Team Spirit", "Evil Geniuses"
        ],
        "Counter-Strike 2": [
            "Astralis", "Natus Vincere", "FaZe Clan", "Team Liquid", "Vitality"
        ],
        "Valorant": [
            "Sentinels", "Fnatic", "Team Liquid", "G2 Esports", "100 Thieves", "Cloud9", "NRG", "TSM"
        ],
        "Overwatch": [
            "San Francisco Shock", "Shanghai Dragons", "Philadelphia Fusion", "Dallas Fuel"
        ],
        "Rocket League": [
            "NRG", "G2 Esports", "Team BDS", "Team Vitality", "Spacestation Gaming"
        ],
        "Fortnite": [
            "TSM", "NRG", "100 Thieves", "FaZe Clan", "Team Liquid"
        ],
        "Apex Legends": [
            "TSM", "NRG", "Team Liquid", "Sentinels", "Cloud9"
        ],
        "Starcraft": [
            "Maru", "Serral", "Reynor", "Dark", "Rogue"
        ],
        "Hearthstone": [
            "Firebat", "Thijs", "RDU", "Kolento", "Hoej"
        ]
    }

    # Bet options for different bet types and sports/games
    BET_OPTIONS = {
        # Common options for all sports/games
        "Match Winner": {
            "type": "dropdown",
            "options": ["Team A", "Team B", "Draw"]
        },
        "Correct Score": {
            "type": "text",
            "placeholder": "Enter score (e.g., 2-1, 3-0)"
        },
        
        # Sport-specific options
        "Football": {
            "Half Time/Full Time": {
                "type": "dropdown",
                "options": ["Team A/Team A", "Team A/Draw", "Team A/Team B",
                          "Draw/Team A", "Draw/Draw", "Draw/Team B",
                          "Team B/Team A", "Team B/Draw", "Team B/Team B"]
            },
            "Total Goals": {
                "type": "dropdown",
                "options": ["Over", "Under"]
            },
            "Both Teams to Score": {
                "type": "dropdown",
                "options": ["Yes", "No"]
            }
        },
        "Basketball": {
            "Total Points": {
                "type": "dropdown",
                "options": ["Over", "Under"]
            }
        },
        "Tennis": {
            "Match Winner": {
                "type": "dropdown",
                "options": ["Team A", "Team B"]
            },
            "Total Sets": {
                "type": "dropdown",
                "options": ["Over", "Under"]
            }
        },
        "Golf": {
            "Top 5 Finish": {
                "type": "dropdown",
                "options": ["Yes", "No"]
            },
            "Match Bet": {
                "type": "dropdown",
                "options": ["Player A", "Player B"]
            }
        },
        "Boxing": {
            "Method of Victory": {
                "type": "dropdown",
                "options": ["KO/TKO", "Decision", "Technical Decision", "Disqualification"]
            },
            "Round Betting": {
                "type": "dropdown",
                "options": ["1-3", "4-6", "7-9", "10-12", "Decision"]
            }
        },
        "MMA": {
            "Method of Victory": {
                "type": "dropdown",
                "options": ["KO/TKO", "Submission", "Decision", "Technical Decision", "Disqualification"]
            },
            "Round Betting": {
                "type": "dropdown",
                "options": ["1", "2", "3", "4", "5", "Decision"]
            }
        },
        
        # Esport-specific options
        "League of Legends": {
            "First Blood": {
                "type": "dropdown",
                "options": ["Team A", "Team B"]
            },
            "First Tower": {
                "type": "dropdown",
                "options": ["Team A", "Team B"]
            },
            "Map Winner": {
                "type": "dropdown",
                "options": ["Team A", "Team B"]
            },
            "Total Kills": {
                "type": "dropdown",
                "options": ["Over", "Under"]
            }
        },
        "Counter-Strike 2": {
            "Team to Win Pistol Round": {
                "type": "dropdown",
                "options": ["Team A", "Team B"]
            },
            "Map Winner": {
                "type": "dropdown",
                "options": ["Team A", "Team B"]
            },
            "Total Rounds": {
                "type": "dropdown",
                "options": ["Over", "Under"]
            }
        }
    }

    # Section requirements for different bet types
    SECTION_REQUIREMENTS = {
        # Common options for all sports/games
        "Match Winner": {
            "location": True,
            "line": False,
            "bet": True
        },
        "Correct Score": {
            "location": True,
            "line": False,
            "bet": True
        },
        "Both Teams to Score": {
            "location": True,
            "line": False,
            "bet": True
        },
        "Total Goals": {
            "location": True,
            "line": True,
            "bet": True
        },
        "Total Points": {
            "location": True,
            "line": True,
            "bet": True
        },
        "Total Kills": {
            "location": True,
            "line": True,
            "bet": True
        },
        "Total Rounds": {
            "location": True,
            "line": True,
            "bet": True
        },
        "Total Sets": {
            "location": True,
            "line": True,
            "bet": True
        }
    }

    @classmethod
    def get_sports(cls) -> List[str]:
        """Get all sports"""
        return cls.SPORT_OPTIONS

    @classmethod
    def get_esports(cls) -> List[str]:
        """Get all esports"""
        return cls.ESPORT_OPTIONS

    @classmethod
    def get_categories(cls) -> List[str]:
        """Get all categories"""
        return list(cls.CATEGORY_LOCATIONS.keys())

    @classmethod
    def get_bet_types(cls, sport_game: str) -> List[Tuple[str, str]]:
        """Get bet types for a specific sport/game"""
        return cls.BET_TYPE_MAPPINGS.get(sport_game, [])

    @classmethod
    def get_tournaments(cls, sport_game: str) -> List[str]:
        """Get tournaments for a specific sport/game"""
        return cls.TOURNAMENTS.get(sport_game, [])

    @classmethod
    def get_locations(cls, sport_game: str) -> List[str]:
        """Get locations for a specific sport/game"""
        return cls.LOCATIONS.get(sport_game, [])

    @classmethod
    def get_teams(cls, sport_game: str) -> List[str]:
        """Get teams for a specific sport/game"""
        return cls.TEAMS.get(sport_game, [])

    @classmethod
    def add_sport(cls, name: str, bet_types: List[Tuple[str, str]], 
                 tournaments: List[str], locations: List[str], teams: List[str]) -> None:
        """Add a new sport with its associated data"""
        cls.SPORT_OPTIONS.append(name)
        cls.BET_TYPE_MAPPINGS[name] = bet_types
        cls.TOURNAMENTS[name] = tournaments
        cls.LOCATIONS[name] = locations
        cls.TEAMS[name] = teams

    @classmethod
    def add_esport(cls, name: str, bet_types: List[Tuple[str, str]], 
                  tournaments: List[str], locations: List[str], teams: List[str]) -> None:
        """Add a new esport with its associated data"""
        cls.ESPORT_OPTIONS.append(name)
        cls.BET_TYPE_MAPPINGS[name] = bet_types
        cls.TOURNAMENTS[name] = tournaments
        cls.LOCATIONS[name] = locations
        cls.TEAMS[name] = teams

    @classmethod
    def add_bet_type(cls, sport_game: str, bet_type: str, description: str) -> None:
        """Add a new bet type for a specific sport/game"""
        if sport_game in cls.BET_TYPE_MAPPINGS:
            cls.BET_TYPE_MAPPINGS[sport_game].append((bet_type, description))

    @classmethod
    def add_tournament(cls, sport_game: str, tournament: str) -> None:
        """Add a new tournament for a specific sport/game"""
        if sport_game in cls.TOURNAMENTS:
            cls.TOURNAMENTS[sport_game].append(tournament)

    @classmethod
    def add_location(cls, sport_game: str, location: str) -> None:
        """Add a new location for a specific sport/game"""
        if sport_game in cls.LOCATIONS:
            cls.LOCATIONS[sport_game].append(location)

    @classmethod
    def add_team(cls, sport_game: str, team: str) -> None:
        """Add a new team for a specific sport/game"""
        if sport_game in cls.TEAMS:
            cls.TEAMS[sport_game].append(team)

    @classmethod
    def get_bet_options(cls, sport_game: str, bet_type: str) -> Dict[str, any]:
        """Get bet options for a specific sport/game and bet type"""
        # First check if there are sport-specific options
        if sport_game in cls.BET_OPTIONS and bet_type in cls.BET_OPTIONS[sport_game]:
            return cls.BET_OPTIONS[sport_game][bet_type]
        
        # Then check common options
        if bet_type in cls.BET_OPTIONS:
            return cls.BET_OPTIONS[bet_type]
        
        # Default to text input if no specific options found
        return {
            "type": "text",
            "placeholder": "Enter bet"
        }

    @classmethod
    def get_section_requirements(cls, sport_game: str, bet_type: str) -> Dict[str, bool]:
        """Get section requirements for a specific sport/game and bet type"""
        # First check if there are sport-specific requirements
        if sport_game in cls.SECTION_REQUIREMENTS and bet_type in cls.SECTION_REQUIREMENTS[sport_game]:
            return cls.SECTION_REQUIREMENTS[sport_game][bet_type]
        
        # Then check common requirements
        if bet_type in cls.SECTION_REQUIREMENTS:
            return cls.SECTION_REQUIREMENTS[bet_type]
        
        # Default to all sections visible if no specific requirements found
        return {
            "location": True,
            "line": True,
            "bet": True
        } 