import pandas as pd

data = pd.read_csv("diamonds.csv")
no_null = data.dropna(subset = ["cut", "carat"])
print(no_null)