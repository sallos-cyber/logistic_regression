import numpy as np

def sigma(z:np.array)->np.array:
    return 1/(1+np.exp(-z))

z=np.array([1,2,3])
a = sigma(z)
print('a: ',a)
