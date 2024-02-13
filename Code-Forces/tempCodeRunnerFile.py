import math

test = int(input())

for _ in range(test):
    count = 1
    n = int(input())
    
    for i in range(2, n+1):
        square = i * i
        cube = i * i * i

        if square > n or cube > n:
            break
        
        if square <= n:
            count += 1
        if cube <= n:
            count += 1

    print(count)
