import requests
from bs4 import BeautifulSoup, Comment
import pandas
import os

url = "https://www.basketball-reference.com/leagues/NBA_2025_per_game.html"

def fetch_parse(url):
    """Fetches NBA player stats from the Basketball reference url

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
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        
        if response.status_code == 200:
            print("GET request successful")
            
            soup = BeautifulSoup(response.content, 'html5lib')
            print(soup.prettify())
            
            table = soup.find("table", {"id": "per_game_stats"})
            
            if table:
                # Convert the HTML table into a DataFrame
                data_frame = pandas.read_html(str(table))[0]
                    
                data_frame = data_frame[data_frame['Player'] != 'Player']
                
                data_frame.reset_index(drop=True, inplace=True)
                
                if not os.path.exists("data"):
                    os.makedirs("data")
                data_frame.to_csv("data/2025_player_stats.csv", index=False)
                print("Saved")
                
                return data_frame
            else:
                print("Could not find Per Stats table")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        
fetch_parse(url)