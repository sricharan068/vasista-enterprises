import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
#elements from index 1 to 3
print("Range of Elements:",arr[1:4])

#all rows, second column
print("Multidimensional Slicing:", arr[:, 1])
