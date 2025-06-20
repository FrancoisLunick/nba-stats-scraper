import pandas
import matplotlib.pyplot

# Read the CSV file into DataFrame
data_frame = pandas.read_csv("data/2025_player_stats.csv")

# Drop rows with invalid values
data_cleaned = data_frame.dropna()

numeric_cols = ['PTS', 'AST', 'TRB', 'FG%', '3P%', "FT%"]
for col in numeric_cols:
    data_frame[col] = pandas.to_numeric(data_frame[col], errors='coerce')

data_sorted = data_frame.sort_values(by='PTS', ascending=False)    
top_10_players = data_sorted.head(10)

top_10_players.plot.barh(x='Player', y='PTS', title="Top 10 Players")
matplotlib.pyplot.xlabel("PTS")
matplotlib.pyplot.ylabel("Player")
matplotlib.pyplot.show()

print(top_10_players)