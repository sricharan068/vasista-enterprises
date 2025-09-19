import numpy as np

angles = np.array([0, 30, 45, 60, 90, 180]) 

radians = np.deg2rad(angles)

print('Sine of angles in the array:')
sine_value = np.sin(radians)
print(np.sin(radians))

print('Inverse Sine of sine values:')
print(np.rad2deg(np.arcsin(sine_value)))

print('Sine hyperbolic of angles in the array:')
sineh_value = np.sinh(radians)
print(np.sinh(radians))

print('Inverse Sine hyperbolic:')
print(np.sin(sineh_value)) 

base = 4
height = 3
print('hypotenuse of right triangle is:')
print(np.hypot(base, height))
