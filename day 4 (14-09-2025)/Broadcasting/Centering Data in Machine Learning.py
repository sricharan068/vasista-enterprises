import numpy as np

data = np.array([
    [10, 20],
    [15, 25],
    [20, 30]
])

feature_mean = data.mean(axis=0)

centered_data = data - feature_mean
print(centered_data)
