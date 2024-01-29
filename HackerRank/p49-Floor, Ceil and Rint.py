import numpy as np
np.set_printoptions(legacy='1.13')

li = list(map(float, input().split()))
ar = np.array(li)
print(np.floor(ar))
print(np.ceil(ar))
print(np.rint(ar))
