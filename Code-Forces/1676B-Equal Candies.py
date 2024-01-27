test = int(input())

for _ in range(test):
    result = 0
    n = int(input())
    li = list(map(int, input().split()))

    minimum = min(li)

    for i in li:
        if i == minimum:
            continue
        result += (i-minimum)

    print(result)
