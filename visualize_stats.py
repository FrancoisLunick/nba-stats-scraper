import pandas
import matplotlib.pyplot

def generate_plots(data_file):
    """This function will clean the data and sort it to top 10 players using 'PTS' then display it un a horizontal bar graph
    
    Args:
        data_file (string): Path to the CSV file that contains player stats
        
    Side Effects:
        - Displays a horizontal bar chart
    """
    # Read the CSV file into DataFrame
    data_frame = pandas.read_csv(data_file)
    
    # Drop rows with invalid values
    data_cleaned = data_frame.dropna()

    numeric_cols = ['PTS', 'AST', 'TRB', 'FG%', '3P%', "FT%"]
    for col in numeric_cols:
        data_cleaned.loc[:, col] = pandas.to_numeric(data_cleaned[col], errors='coerce')

    data_sorted = data_cleaned.sort_values(by='PTS', ascending=False)    
    top_10_players = data_sorted.head(10)

    top_10_players.plot.barh(x='Player', y='PTS', title="Top 10 Players")
    matplotlib.pyplot.xlabel("PTS")
    matplotlib.pyplot.ylabel("Player")
    matplotlib.pyplot.show()