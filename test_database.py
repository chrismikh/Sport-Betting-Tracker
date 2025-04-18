from database.bet_database import BetDatabase
import os

def test_database():
    # Initialize the database
    db = BetDatabase()
    
    # Create a test bet
    test_bet = {
        'category': 'Sport',
        'sport_game': 'Football',
        'tournament': 'Premier League',
        'team_a': 'Manchester United',
        'team_b': 'Liverpool',
        'location': 'Old Trafford',
        'bet': 'Manchester United to win',
        'bet_type': 'Prematch',
        'odds': 2.50,
        'stake': 100.00,
        'result': 'Won',
        'cash_out_amount': None
    }
    
    # Add the bet to database
    bet_id = db.add_bet(test_bet)
    print(f"Added bet with ID: {bet_id}")
    
    # Get all bets
    all_bets = db.get_all_bets()
    print("\nAll bets in database:")
    for bet in all_bets:
        print(f"\nBet ID: {bet['id']}")
        print(f"Category: {bet['category']}")
        print(f"Sport/Game: {bet['sport_game']}")
        print(f"Teams: {bet['team_a']} vs {bet['team_b']}")
        print(f"Bet: {bet['bet']}")
        print(f"Odds: {bet['odds']}")
        print(f"Stake: {bet['stake']}")
        print(f"Result: {bet['result']}")
        print(f"Date: {bet['date']}")
    
    # Close the database connection
    db.close()
    
    # Show where the database file is located
    db_path = os.path.abspath("bets.db")
    print(f"\nDatabase file location: {db_path}")
    print("\nYou can also view the database using SQLite Browser (https://sqlitebrowser.org/)")

if __name__ == "__main__":
    test_database() 