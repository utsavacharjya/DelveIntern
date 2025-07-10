import pandas as pd

data = pd.read_excel("DS Internship - EDA - Data.xlsx", sheet_name="Data")
open_1991 = data[data["Store Open"].dt.year == 1991]["Store"].nunique()
print(open_1991)