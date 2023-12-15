while True:
    sum = 0
    n = int(input())
    if n == 0:
        break

    if n%2 == 0:
        for i in range(5):
            sum += n
            n += 2
    else:
        n += 1
        for i in range(5):
            sum += n
            n += 2


    print(sum)
