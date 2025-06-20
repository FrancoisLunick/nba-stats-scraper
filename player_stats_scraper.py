import requests
from bs4 import BeautifulSoup, Comment

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
            
            # Find all of the HTML comments in the page
            comments = soup.find_all(string=lambda text: isinstance(text, Comment))
            print(comments)
            
            for comment in comments:
                if 'per_game_stats' in comment:
                    # Parse the comment's content as HTML
                    new_soup = BeautifulSoup(comment, 'html5lib')
                    # Find the stats table
                    table = new_soup.find('table', id='per_game_stats')
                    
                    print(table)
        else:
            # Print status code and response if the request is not successful
            print(f"GET request failed with status code: {response.status_code}")
            print(f"Response text: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        
fetch_parse(url)