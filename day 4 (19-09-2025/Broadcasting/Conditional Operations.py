import numpy as np

ages = np.array([12, 24, 35, 45, 60, 72])

age_group = np.array(["Adult", "Minor"])

result = np.where(ages > 18, age_group[0], age_group[1])

print(result)
