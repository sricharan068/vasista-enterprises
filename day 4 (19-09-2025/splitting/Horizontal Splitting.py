import numpy as np

array = np.array([[1, 2, 3, 4],
                           [5, 6, 7, 8],
                           [9, 10, 11, 12]])

result = np.hsplit(array, 2)

print("2D Array:")
print(array)
print("\nResult after numpy.hsplit():")
print(result)
