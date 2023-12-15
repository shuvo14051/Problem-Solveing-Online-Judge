n = int(input())
inside, outside = 0, 0

for i in range(n):
    number = int(input())
    if number >= 10 and number <= 20:
        inside += 1
    else:
        outside += 1

print("%d in" %inside)
print("%d out" %outside)
