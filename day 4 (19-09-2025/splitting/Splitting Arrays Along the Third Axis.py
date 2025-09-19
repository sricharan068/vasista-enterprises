import numpy as np

original_3d_array = np.arange(24).reshape((2, 3, 4))

result = np.dsplit(original_3d_array, 2)

print("Original 3D Array:")
print(original_3d_array)
print("\nResult after numpy.dsplit():")
print(result)
