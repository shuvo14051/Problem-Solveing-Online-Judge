while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    li = [0]*10
    for num in range(a, b+1):
        while num > 0:
            digit = num % 10
            li[digit] += 1
            num //= 10

    print(" ".join(str(x) for x in li))
