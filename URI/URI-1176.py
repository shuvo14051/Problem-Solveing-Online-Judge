test = int(input())
for i in range(test):
    n = int(input())
    ar = [0,1]
    first = 0
    second = 1
    for j in range(n):
        ar.append(ar[first]+ar[second])
        first += 1
        second += 1
    result = ar[n]
    print("Fib({}) = {}".format(n, result))