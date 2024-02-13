import math

test = int(input())

for _ in range(test):
    n = int(input())
    
    square_root = int(math.sqrt(n))
    cube_root = int(n ** (1/3))
    
    count = square_root + cube_root - 1  # Counting the overlaps of square and cube
    
    print(count)
