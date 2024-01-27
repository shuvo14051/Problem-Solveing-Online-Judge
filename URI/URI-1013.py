a, b, c = [int(x) for x in input().split()]


max_ab = (a + b + abs(a - b)) // 2

max = (max_ab + c + abs(max_ab - c)) // 2

print("%d eh o maior" %max)
