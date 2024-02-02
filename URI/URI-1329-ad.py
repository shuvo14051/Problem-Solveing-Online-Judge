

while True:
    n = int(input())
    if n == 0:
        break
    li = list(map(int, input().split()))[:n]
    mary = li.count(0)
    john = li.count(1)

    print("Mary won {} times and John won {} times".format(mary, john))