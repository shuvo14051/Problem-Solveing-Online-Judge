n = int(input())

def factorial(n,k):
    fact = 1
    for i in range(n, 1, -k):
        fact = fact *i
    return fact


for i in range(n):
    num, k = "", ""
    value = input()
    for j in value:
        if j != "!":
            num += j
        else:
            k += j
    num = int(num)
    k = len(k)

    res = factorial(num, k)
    print(res)
    