test = int(input())

for i in range(test):
    n = int(input())
    count = 0
    for j in range(2,n):
        if n%j == 0:
            count += 1

    if count == 0:
        print("%d eh primo" %n)
    else:
        print("%d nao eh primo" %n)