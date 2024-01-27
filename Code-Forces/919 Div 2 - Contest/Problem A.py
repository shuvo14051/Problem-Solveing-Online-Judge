# Number of test cases
t = int(input())

for _ in range(t):
    # Number of constraints for each test case
    n = int(input())

    # Initialize min and max values
    min_val = float('-inf')
    max_val = float('inf')

    for _ in range(n):
        a, x = map(int, input().split())
        if a == 1:
            min_val = max(min_val, x)
        elif a == 2:
            max_val = min(max_val, x)
    
    # If there are additional constraints, update min_val and max_val
    min_val = max(min_val, 1)
    max_val = min(max_val, 10**9)

    # Calculate and print the number of integers k satisfying all constraints
    result = max(0, max_val - min_val )
    print(result)
