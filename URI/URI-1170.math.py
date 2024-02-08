test = int(input())

for _ in range(test):
    capacity = float(input())
    count = 0
    while capacity > 1:
        capacity /= 2
        count += 1

    print("{} dias".format(count))
