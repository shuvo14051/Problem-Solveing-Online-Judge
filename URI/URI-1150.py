x = int(input())
z = int(input())
count = 0
while z<=x :
    z = int(input())

sum = 0
while True:
    sum += x
    count += 1
    x += 1
    if sum > z:
        break

print(count)
