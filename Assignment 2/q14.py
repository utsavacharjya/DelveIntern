import pandas as pd

data = pd.read_csv("diamonds.csv")
data["volume"] = data.apply(lambda row: row["x"] * row["y"] * row["z"] if row["depth"] > 60 else 8, axis = 1)
print(data)