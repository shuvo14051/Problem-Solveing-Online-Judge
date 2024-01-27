test = int(input())

for _ in range(test):
    capacity = float(input())
    count = 0
    while capacity > 0:
        count += 1
        capacity //= 2

    print("{} dias".format(count))
