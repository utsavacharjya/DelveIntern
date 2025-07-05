import pandas as pd

data = pd.read_csv("imdb.csv", on_bad_lines = "skip")
sorted_data = data.sort_values(by = ["year", "imdbRating"], ascending = [True, False])
print(sorted_data)