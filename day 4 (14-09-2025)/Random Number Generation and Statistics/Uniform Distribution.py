import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

low = 10  
high = 20  
size = 1000  

data = np.random.uniform(low=low, high=high, size=size)
sns.histplot(data, bins=30, kde=False, color='skyblue', edgecolor='black')

plt.title(f"Uniform Distribution (Range: {low} to {high})")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
