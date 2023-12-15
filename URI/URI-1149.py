a, n = map(int, input().split())

while n <= 0:
    n = int(input())

sum = 0

while n!= 0:
    sum += a
    a += 1
    n -= 1

print(sum)