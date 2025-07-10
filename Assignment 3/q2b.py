import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""We decide the month based on highest average sales per month.
   We plot a line plot to decide best month."""

data = pd.read_excel("DS Internship - EDA - Data.xlsx", sheet_name="Data")
mon_sal = data.groupby("Month")["Sales"].mean().reset_index()
best_tim = mon_sal.sort_values(by = "Month")

sns.lineplot(data = best_tim, x = "Month", y = "Sales", marker = "o")
plt.show()