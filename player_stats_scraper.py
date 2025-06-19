url = "https://www.basketball-reference.com/leagues/NBA_2025_per_game.html"

def fetch_parse(url):
    """_summary_

    Args:
        url (string): the url to scrape NBA stats from
        
    Returns:
        pandas.DataFrame: A DataFrame which contains the stats of NBA players
        
    Side Effects:
        Saves the DataFrame to 'data/2025_player_stats.csv'
    
    Raises:
        Exception: If the request fails
    """