from database.bet_database import BetDatabase

# Initialize database
with BetDatabase() as db:
    print("--- Adding and retrieving sports/games ---")
    sport_game_id = db.add_sport_game("Testball", "Sport")
    print("Added sport/game ID:", sport_game_id)
    print("All sports/games:", db.get_all_sport_games())

    print("\n--- Adding and retrieving teams ---")
    team_id = db.add_team("Testballers", sport_game_id)
    print("Added team ID:", team_id)
    print("Teams for Testball:", db.get_teams_for_sport_game(sport_game_id))

    print("\n--- Adding and retrieving tournaments ---")
    tournament_id = db.add_tournament("Testball World Cup", sport_game_id)
    print("Added tournament ID:", tournament_id)
    print("Tournaments for Testball:", db.get_tournaments_for_sport_game(sport_game_id))

    print("\n--- Adding and retrieving locations ---")
    location_id = db.add_location("Testball Arena", sport_game_id)
    print("Added location ID:", location_id)
    print("Locations for Testball:", db.get_locations_for_sport_game(sport_game_id))

    print("\n--- Adding and retrieving bet types ---")
    bet_type_id = db.add_bet_type("Test Winner", sport_game_id, "Who wins the test match?")
    print("Added bet type ID:", bet_type_id)
    print("Bet types for Testball:", db.get_bet_types_for_sport_game(sport_game_id))

    print("\n--- Adding and retrieving bet type options ---")
    option_id = db.add_bet_type_option(bet_type_id, "dropdown", options='["Team A", "Team B", "Draw"]', placeholder=None)
    print("Added bet type option ID:", option_id)
    print("Bet type options for 'Test Winner':", db.get_bet_type_options(bet_type_id)) 