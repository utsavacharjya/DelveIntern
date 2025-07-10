import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel("DS Internship - EDA - Data.xlsx", sheet_name="Data")
st_mod = data[["Store", "Store Modification"]].drop_duplicates()
remod = st_mod[st_mod["Store Modification"] != "no change"]

sns.countplot(data = remod, x = "Store Modification")
plt.xlabel("Modification Type")
plt.ylabel("Number of Stores")
plt.show()