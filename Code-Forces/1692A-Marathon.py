test = int(input())

for _ in range(test):
    count = 0
    a, b, c, d = map(int, input().split())
    if b>a:
        count += 1
    if c>a:
        count += 1
    if d>a:
        count += 1

    print(count)