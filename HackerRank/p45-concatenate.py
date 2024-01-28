import numpy as np

n, m, p = map(int, input().split())

# Using list comprehension to get input for the 2D list
li = [[int(x) for x in input().split()] for _ in range(n+m)]

ar = np.array(li)

print(ar)