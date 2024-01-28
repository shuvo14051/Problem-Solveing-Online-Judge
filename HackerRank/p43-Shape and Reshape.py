import numpy as np

li = list(map(int, input().split()))
array = np.array(li)
result = array.reshape((3,3))
print(result)
