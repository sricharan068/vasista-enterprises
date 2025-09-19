import numpy as np

weight = np.array([50.7, 52.5, 50, 58, 55.63, 73.25, 49.5, 45])

print('Minimum and maximum weight of the students: ')
print(np.amin(weight), np.amax(weight))

print('Range of the weight of the students: ')
print(np.ptp(weight))

print('Weight below which 70 % student fall: ')
print(np.percentile(weight, 70))
 
print('Mean weight of the students: ')
print(np.mean(weight))

print('Median weight of the students: ')
print(np.median(weight))

print('Standard deviation of weight of the students: ')
print(np.std(weight))

print('Variance of weight of the students: ')
print(np.var(weight))

print('Average weight of the students: ')
print(np.average(weight))
