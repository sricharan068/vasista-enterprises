import numpy as np


arr1d = np.array([10, 20, 30, 40, 50])


print("Single element access:", arr1d[2])  

print("Negative indexing:", arr1d[-1])  

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Multidimensional array access:", arr2d[1, 0])
