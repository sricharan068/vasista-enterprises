import numpy as np
np.seterr(all='raise')

try:
    np.divide(1, 0)
except FloatingPointError as e:
    print("FloatingPointError caught:", e)
