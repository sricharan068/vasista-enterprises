import numpy as np

even = np.array([0, 2, 4, 6, 8, 16, 32])
odd = np.array([1, 3, 5, 7, 9, 17, 33])

print('bitwise_and of two arrays: ')
print(np.bitwise_and(even, odd))

print('bitwise_or of two arrays: ')
print(np.bitwise_or(even, odd))

print('bitwise_xor of two arrays: ')
print(np.bitwise_xor(even, odd))
 
print('inversion of even no. array: ')
print(np.invert(even))

print('left_shift of even no. array: ')
print(np.left_shift(even, 1))

print('right_shift of even no. array: ')
print(np.right_shift(even, 1))
