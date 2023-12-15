even = 0
odd = 0
for i in range(5):
    n = int(input())

    if n % 2 == 0:
        even += 1

print("%d valores pares" % even)

