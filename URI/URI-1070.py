n = int(input())

for i in range(6):
    if n%2 != 0:
        print(n)
        n += 2

    else:
        n += 1
        print(n)
        n+=2