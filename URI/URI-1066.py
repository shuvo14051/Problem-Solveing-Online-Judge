positive = 0
negative = 0
even = 0
odd = 0
for i in range(5):
    n = int(input())

    if n > 0:
        positive += 1
    if n < 0:
        negative += 1
    if n % 2 == 0:
        even += 1
    if n % 2 != 0:
        odd += 1

print("%d valor(es) par(es)" % even)
print("%d valor(es) impar(es)" % odd)
print("%d valor(es) positivo(s)" % positive)
print("%d valor(es) negativo(s)" % negative)
