import pandas as pd

data = pd.read_csv("diamonds.csv")
mean = data["price"].mean()
not_na = data["price"].fillna(value = mean)
print(data)