from math import *

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    b = 2*(x**2) + (5*y)**2
    c = -100*x + y**3
    r = (3*x)**2 + y**2

    m = max(r, b, c)

    if m == r:
        print("Rafael ganhou")
    elif m == b:
        print("Beto ganhou")
    else:
        print("Carlos ganhou") 
