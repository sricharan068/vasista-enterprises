# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load dataset
data = pd.read_csv("C:\\Users\\Vanshi\\Desktop\\bestsellers.csv")

# Compute correlation matrix
co_mtx = data.corr(numeric_only=True)

# Print correlation matrix
print(co_mtx)

# Plot correlation heatmap
sns.heatmap(co_mtx, cmap="YlGnBu", annot=True)

# Display heatmap
plt.show()
