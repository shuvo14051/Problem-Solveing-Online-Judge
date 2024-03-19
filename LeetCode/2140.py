base = [100, 50, 20, 10, 5, 2]

while True:
    n, m = map(int, input().split())
    count = 0
    if n == 0 and m==0:
        break
    change = m - n
    if change == 0:
        print("possible")
        continue

    change_possible = False
    for i in base:
        while change >= i:
            change -= i
            count += 1
            if change == 0:
                change_possible = True
                break
    if change_possible and count == 2:
        print("possible")
    else:
        print("impossible")
