import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel("DS Internship - EDA - Data.xlsx", sheet_name="Data")
prof_div = data.groupby("Super Division")["Sales"].sum().reset_index()

sns.barplot(data = prof_div, x = "Super Division", y = "Sales")
plt.show()