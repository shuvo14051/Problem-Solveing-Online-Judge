test = int(input())

for i in range(test):
    n = int(input())
    sum = 0
    for j in range(1,n):
        if n%j == 0:
            sum += j

    if sum == n:
        print("%d eh perfeito" %n)
    else:
        print("%d nao eh perfeito" %n)