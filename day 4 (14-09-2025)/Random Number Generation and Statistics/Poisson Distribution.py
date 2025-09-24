import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

lam = 2  
size = 1000  

data = random.poisson(lam=lam, size=size)

sns.displot(data, kde=False, bins=np.arange(-0.5, max(data)+1.5, 1), color='skyblue', edgecolor='black')

plt.title(f"Poisson Distribution (λ={lam})")
plt.xlabel("Number of Events")
plt.ylabel("Frequency")
plt.grid(True)

plt.show()
