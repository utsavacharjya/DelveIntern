import pandas as pd

data = pd.read_excel("SalesData.xlsx")
salesman_manager = data.groupby("Manager")["SalesMan"].unique()
salesman_manager.columns = ["manager", "list_of_salesmen"]
print(salesman_manager)