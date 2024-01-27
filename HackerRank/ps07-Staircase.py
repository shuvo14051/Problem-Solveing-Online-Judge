n = int(input())

for i in range(1,n+1):
    for j in range(n-1, i-1, -1):
        print(" ", end='')

    for j in range(0,i):
        print("#", end='')

    print()