import numpy as np

n, m = map(int, input().split())

li = [[int(x) for x in input().split()] for _ in range(n)]

ar = np.array(li)

s = np.sum(ar, axis=0)
print(np.prod(s, axis=0))

