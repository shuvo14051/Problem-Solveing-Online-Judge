# Solved
test = int(input())
for i in range(test):
    n = int(input())
    sum1 = n * (n + 1) // 2
    sum2 = n*(n+1)*(2*n+1)//6
    result = (sum1**2) - sum2
    print(result)
