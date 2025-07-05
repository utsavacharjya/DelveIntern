import pandas as pd

data = pd.read_excel("SalesData.xlsx")
tot_sal = data.groupby("Region").agg({"SalesMan": "count", "Sale_amt": "sum"})
tot_sal.columns = ["salesmen_count", "total_sales"]
print(tot_sal)