import requests

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
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print("GET request successful")
        else:
            print(f"GET request failed with status code: {response.status_code}")
            print(f"Response text: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        
fetch_parse(url)