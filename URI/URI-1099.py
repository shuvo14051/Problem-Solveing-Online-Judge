test = int(input())

for i in range(test):
    a,b = map(int, input().split())
    if a>b:
        a,b = b,a
    # a,b = [int(x) for x in input().split()] # another way to take input
    sum = 0
    for i in range(a+1, b):
        if i%2 != 0:
            sum += i

    print(sum)
