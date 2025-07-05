import pandas as pd

data = pd.read_csv("imdb.csv", on_bad_lines = "skip")
lon_idx = data["duration"].idxmax()
sho_idx = data["duration"].idxmin()
lon = data.loc[lon_idx, "title"]
sho = data.loc[sho_idx, "title"]
print("Longest title: {0}\nShortest title: {1}".format(lon, sho))