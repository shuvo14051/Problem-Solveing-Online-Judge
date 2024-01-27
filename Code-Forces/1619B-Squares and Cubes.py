import math

test = int(input())

for _ in range(test):
    count = 0
    n = int(input())
    
    # Loop up to the square root of n
    for i in range(1, int(math.sqrt(n)) + 1):
        square = i * i
        cube = i * i * i
        
        # Check for both perfect square and perfect cube conditions
        if square <= n:
            count += 1
        if cube <= n:
            count += 1

    print(count)
