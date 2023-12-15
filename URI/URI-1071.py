a = int(input())
b = int(input())

if a > b:
    a, b = b, a

sum = 0
for i in range(a+1, b):
    if i % 2 != 0:
        sum += i

print(sum)
