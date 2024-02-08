def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

while True:
    n = input()
    if n =="0":
        break
    l = len(n)
    s = 0
    index = 0
    for i in range(l, 0, -1):
        s = s + int(n[index]) * factorial(i)
        index += 1
    print(s)