import numpy as np

array = np.array([[3, 2, 1], [8, 9, 7], [4, 6, 5]])

result = np.split(array, 3, axis=1)

print("2D Array:")
print(original_array)
print("\nResult after numpy.split() along axis=1:")
print(result)
