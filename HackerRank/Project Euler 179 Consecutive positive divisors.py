test = int(input())

for i in range(test):
    n = int(input())
    for j in range(2, n):
        if n % j == 0:
            print(j)
