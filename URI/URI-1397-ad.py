while True:
    n = int(input())
    if n == 0:
        break
    left, right = 0, 0
    for i in range(n):
        a, b = map(int, input().split())
        if a > b: 
            left += 1
        elif b > a:
            right += 1
    print(left, right)
        