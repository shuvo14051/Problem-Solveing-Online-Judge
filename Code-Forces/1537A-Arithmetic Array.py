test = int(input())

for _ in range(test):
    n = int(input())
    li = list(map(int, input().split()))
    s = sum(li)
    if s < 0:
        res = s + n
        res = abs(res)
    else:
        res = s - n

    print(res)
