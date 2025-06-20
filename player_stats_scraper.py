import requests
from bs4 import BeautifulSoup, Comment
import pandas
import os
from io import StringIO

def fetch_parse():
    """Fetches NBA player stats from the Basketball reference url
        
    Returns:
        pandas.DataFrame: A DataFrame which contains the stats of NBA players
        
    Side Effects:
        Saves the DataFrame to 'data/2025_player_stats.csv'
    
    Raises:
        Exception: If the request fails
    """
    
    url = "https://www.basketball-reference.com/leagues/NBA_2025_per_game.html"
    
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        
        if response.status_code == 200:
            print("GET request successful")
            
            soup = BeautifulSoup(response.content, 'html5lib')
            
            table = soup.find("table", {"id": "per_game_stats"})
            
            if table:
                # Convert the HTML table into a DataFrame
                data_frame = pandas.read_html(StringIO(str(table)))[0]
                    
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