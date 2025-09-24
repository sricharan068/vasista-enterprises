import numpy as np

m=np.array([[[1,2,3],
            [4,5,6],
            [7,8,9]],

            [[10,11,12],
            [13,14,15],
            [16,17,18]]])

n=np.array([[[51,52,53],
            [54,55,56],
            [57,58,59]],

            [[110,111,112],
            [113,114,115],
            [116,117,118]]])


print(np.stack((m,n),axis=0))
print(np.stack((m,n),axis=1))
print(np.stack((m,n),axis=2))
print(np.stack((m,n),axis=3))
