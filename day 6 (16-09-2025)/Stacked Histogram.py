import matplotlib.pyplot as plt
import numpy as np

# Generate random data for stacked histograms
data1 = np.random.randn(1000)
data2 = np.random.normal(loc=3, scale=1, size=1000)

# Creating a stacked histogram
plt.hist([data1, data2], bins=30, stacked=True, color=['cyan', 'Purple'], edgecolor='black')

# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Stacked Histogram')

# Adding legend
plt.legend(['Dataset 1', 'Dataset 2'])

# Display the plot
plt.show()
