import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""We decide the state based on highest average sales per store.
   If the average sales are the same then the state with lower store gets priority.
   Then we pick the top 3 candidate states."""

data = pd.read_excel("DS Internship - EDA - Data.xlsx", sheet_name="Data")
stat_sal = data.groupby("State").agg(tot_sal = ("Sales", "sum"), str_cnt = ("Store", "nunique")).reset_index()
stat_sal["avg_sal"] = stat_sal["tot_sal"] / stat_sal["str_cnt"]
cand_stat = stat_sal.sort_values(by = ["avg_sal", "str_cnt"], ascending=[False, True]).head(3)

sns.barplot(data = cand_stat, x = "State", y = "avg_sal")
plt.xlabel("Avg Sales per Store")
plt.show()