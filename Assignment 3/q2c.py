import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""We plot a count plot to find which outlet type has an odd number of closures comapred to active outlets."""

data = pd.read_excel("DS Internship - EDA - Data.xlsx", sheet_name="Data")
data["Status"] = data["Store Close"].apply(lambda x: "Closed" if x != "No Close date" else "Active")
clos = data[["Store", "Status", "Outlet Type"]].drop_duplicates()

sns.countplot(data = clos, x = "Outlet Type", hue = "Status")
plt.ylabel("Number of Stores")
plt.show()