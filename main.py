from player_stats_scraper import fetch_parse
from visualize_stats import generate_plots

file_name= "data/2025_player_stats.csv"
url = "https://www.basketball-reference.com/leagues/NBA_2025_per_game.html"

def main():
    # Scrape NBA data
    fetch_parse(url)
    
    # Generate Plots
    generate_plots(file_name)
    
if __name__ == "__main__":
    main()