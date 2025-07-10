import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel("DS Internship - EDA - Data.xlsx", sheet_name="Data")
sal_sz = data.groupby("Total Sq Ft")["Sales"].sum().reset_index()

plt.figure(figsize = (15, 15))
sns.regplot(data = sal_sz, x = "Total Sq Ft", y = "Sales")
plt.show()