import pandas as pd

data = pd.read_csv("imdb.csv", on_bad_lines = "skip")
fif_imdb = data["imdbRating"].iloc[4]
print(fif_imdb)