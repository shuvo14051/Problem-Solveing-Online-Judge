import numpy as np

n, m = map(int, input().split())

li1 = [[int(x) for x in input().split()] for _ in range(n)]
li2 = [[int(x) for x in input().split()] for _ in range(n)]

ar1 = np.array(li1)
ar2 = np.array(li2)

print((ar1+ar2))
print((ar1-ar2))
print((ar1*ar2))
print((ar1//ar2))
print((ar1%ar2))
print((ar1**ar2))