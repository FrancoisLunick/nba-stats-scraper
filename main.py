from player_stats_scraper import fetch_parse
from visualize_stats import generate_plots

file_name= "data/2025_player_stats.csv"

def main():
    # Scrape NBA data
    fetch_parse()
    
    # Generate Plots
    generate_plots(file_name)
    
if __name__ == "__main__":
    main()