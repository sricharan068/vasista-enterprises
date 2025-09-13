import math
try:
    result = math.exp(1000)  
except OverflowError as e:
    print(e)
