import numpy as np
food_data = np.array([[0.8, 2.9, 3.9], 
                      [52.4, 23.6, 36.5],
                      [55.2, 31.7, 23.9],
                      [14.4, 11, 4.9]])

caloric_values = np.array([9,4,4]) 

caloric_matrix = caloric_values 

calorie_breakdown = food_data * caloric_matrix
print(calorie_breakdown)
