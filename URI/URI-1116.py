test = int(input())

for i in range(test):
    a, b = map(int, input().split())

    if b == 0:
        print("divisao impossivel")

    else:
        div = a / b

        print("%.1f" % div)
