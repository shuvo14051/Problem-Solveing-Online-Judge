while True:
    n = int(input())
    summ = 0
    if n==0:
        break
    for i in range(1, n+1):
        summ += i**2

    print(summ) 