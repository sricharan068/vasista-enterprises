import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(42)
data = pd.DataFrame(np.random.rand(50, 4), columns=['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4'])

num_features = len(data.columns)

fig, axes = plt.subplots(num_features, num_features, figsize=(10, 10))

for i in range(num_features):
    for j in range(num_features):
        ax = axes[i, j]

        if i == j:
            ax.hist(data.iloc[:, i], bins=10, color="skyblue", edgecolor="black")
        else:
            x = data.iloc[:, j]
            y = data.iloc[:, i]
            ax.scatter(x, y, alpha=0.7, s=10, color="blue")

            m, b = np.polyfit(x, y, 1)  
            ax.plot(x, m*x + b, color="red", linewidth=1)

        if j == 0:
            ax.set_ylabel(data.columns[i], fontsize=10)
        if i == num_features - 1:
            ax.set_xlabel(data.columns[j], fontsize=10)

        ax.set_xticks([])
        ax.set_yticks([])

plt.tight_layout()
plt.show()
