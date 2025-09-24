import numpy as np


array = np.arange(13)


result = np.array_split(array, 4)

print("Array:")
print(array)
print("\nResult after numpy.array_split():")
print(result)
