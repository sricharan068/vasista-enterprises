import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = 1  
size = 1000  

data = np.random.chisquare(df=df, size=size)

sns.displot(data, kind="kde", color='purple', label=f'Chi-Square (df={df})')

plt.title(f"Chi-Square Distribution (df={df})")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(True)

plt.show()
