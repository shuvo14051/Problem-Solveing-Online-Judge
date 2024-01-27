while True:
    maximum = 0
    peak = 0
    n = int(input())
    if n == 0:
        break

    ar = list(map(int, input().split()))[:n]
    maximum = max(ar)
    for i in ar:
        if i == maximum:
            peak += 1

    print(peak * 2)
