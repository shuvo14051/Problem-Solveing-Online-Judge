while True:
    n = int(input())
    if n == 0:
        break
    if n <= 100:
        print("f91({}) = {}".format(n, 91))
    else:
        print("f91({}) = {}".format(n, n-10))
