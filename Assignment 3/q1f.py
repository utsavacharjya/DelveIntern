import pandas as pd

data = pd.read_excel("DS Internship - EDA - Data.xlsx", sheet_name="Data")
close = data[data["Store Close"] != "No Close date"]["Store"].nunique()
print(close)