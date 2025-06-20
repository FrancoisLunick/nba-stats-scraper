import pandas

# Read the CSV file into DataFrame
data_frame = pandas.read_csv("data/2025_player_stats.csv")

# Drop rows with invalid values
data_cleaned = data_frame.dropna()

numeric_cols = ['PTS', 'AST', 'TRB', 'FG%', '3P%', "FT%"]
for col in numeric_cols:
    data_frame[col] = pandas.to_numeric(data_frame[col], errors='coerce')

print(data_frame.head)