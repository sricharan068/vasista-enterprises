import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=0, scale=1, size=1000)

plt.hist(data, bins=30, edgecolor='black', density=True)
pdf = data.pdf(x, loc=loc, scale=scale)  
plt.plot(x, pdf, color='red', label='Theoretical PDF')
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True)
plt.show()
