import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel("DS Internship - EDA - Data.xlsx", sheet_name="Data")
yr_sal = data.groupby("Year")["Sales"].sum().reset_index()

sns.barplot(data = yr_sal, x = "Year", y = "Sales")
plt.show()