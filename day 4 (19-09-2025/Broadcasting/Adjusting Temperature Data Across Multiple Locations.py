import numpy as np

temperatures = np.array([
    [30, 32, 34, 33, 31],  
    [25, 27, 29, 28, 26], 
    [20, 22, 24, 23, 21]  
])

corrections = np.array([1.5, -0.5, 2.0])

adjusted_temperatures = temperatures + corrections[:, np.newaxis]
print(adjusted_temperatures)
