import pandas as pd
import numpy as np

data = pd.read_csv("diamonds.csv")
num = data.select_dtypes(include = "number")
print(num)