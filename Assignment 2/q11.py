import pandas as pd

data = pd.read_csv("diamonds.csv")
dup = data.duplicated().sum()
print(dup)