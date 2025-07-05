import pandas as pd

data = pd.read_excel("SalesData.xlsx")
data["Year"] = data["OrderDate"].dt.year
total_sales = data.groupby(["Year", "Region"])["Sale_amt"].sum()
print(total_sales)