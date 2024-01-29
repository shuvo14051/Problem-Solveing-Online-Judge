import numpy as np

n, m = map(int, input().split())

li = [[int(x) for x in input().split()] for _ in range(n)]

ar = np.array(li).reshape(n, m)

s = np.min(ar, axis=1)
print(np.max(s))

