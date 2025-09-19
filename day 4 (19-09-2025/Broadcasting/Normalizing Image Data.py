import numpy as np

image = np.array([
    [100, 120, 130],
    [90, 110, 140],
    [80, 100, 120]
])

mean = image.mean(axis=0)   
std = image.std(axis=0)    

normalized_image = (image - mean) / std
print(normalized_image)
