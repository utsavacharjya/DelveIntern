import pandas as pd

data = pd.read_csv("imdb.csv", on_bad_lines = "skip")
sma_fil = data[(data["duration"] >= 1800) & (data["duration"] <= 10800)]
print(sma_fil)