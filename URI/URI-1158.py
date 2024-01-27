test = int(input())

for i in range(test):
    sum = 0

    n, k = map(int,input().split())

    if n%2 != 0:
        for j in range(k):
            sum += n
            n += 2
    else:
        n += 1
        for k in range(k):
            sum += n
            n += 2


    print(sum)
