import numpy as np

n, m = map(int, input().split())

# Using list comprehension to get input for the 2D list
li = [[int(x) for x in input().split()] for _ in range(n)]

ar = np.array(li)

print(ar.transpose())
print(ar.flatten())