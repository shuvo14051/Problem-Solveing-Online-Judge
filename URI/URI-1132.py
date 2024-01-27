a = int(input())
b = int(input())
sum = 0

if a > b:
    a, b = b, a

for i in range(a, b + 1):
    if i % 13 != 0:
        sum += i

print(sum)
