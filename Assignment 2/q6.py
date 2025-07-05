import pandas as pd

data = pd.read_excel("SalesData.xlsx")
total_sale = data["Sale_amt"].sum()
manager_sale = data.groupby("Manager")["Sale_amt"].sum()
manager_sale = (manager_sale / total_sale) * 100
print(manager_sale)