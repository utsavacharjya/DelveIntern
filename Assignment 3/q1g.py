import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel("DS Internship - EDA - Data.xlsx", sheet_name="Data")
avg_sz = data.groupby("Super Division")["Total Sq Ft"].mean().reset_index()


sns.pointplot(data = avg_sz, x = "Super Division", y = "Total Sq Ft")
plt.show()