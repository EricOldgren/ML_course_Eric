import numpy as np

## Task A ##

def standardize(D):
    zero_mean_D = D - np.mean(D,axis = 0)
    unit_variance_D = zero_mean_D / np.std(zero_mean_D,axis = 0)
    print(np.std(unit_variance_D,axis=0))
    print(np.mean(unit_variance_D,axis=0))
    return unit_variance_D

#D = np.array([[1,6],[2,4]])
D = np.random.randn(4,6)
print(D)
D_standard = standardize(D)
print(D_standard)
