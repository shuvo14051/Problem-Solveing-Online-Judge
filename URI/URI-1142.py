n =  int(input())
x = 0
for i in range(1, n+1):
    print("%d " % i, end='')
    x += 1
    if x == 4:
        print()
        x = 0