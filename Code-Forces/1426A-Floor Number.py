test = int(input())

def find_floor(n, x):
    if n <= 2:
        return 1

    floor = 1
    apartments_on_floor = 2

    while n > apartments_on_floor:
        floor += 1
        apartments_on_floor += x

    return floor

for _ in range(test):
    apartment, floors = map(int, input().split())
    floor = find_floor(apartment, floors)
    print(floor)

