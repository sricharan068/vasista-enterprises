import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

scale = 2  
size = 1000  

data = np.random.exponential(scale=scale, size=size)

sns.histplot(data, bins=30, kde=True, color='orange', edgecolor='black')

plt.title(f"Exponential Distribution (Scale={scale})")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)

plt.show()
