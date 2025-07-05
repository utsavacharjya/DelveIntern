import pandas as pd

data = pd.read_excel("SalesData.xlsx")
min_sale = data.groupby("Item")["Sale_amt"].min()
print(min_sale)