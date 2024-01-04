n = int(input())
base = 0
for i in range(1000):
    print("N[{}] = {}".format(i,base))
    base += 1
    if base == n:
        base = 0
