count = 0
sum = 0
while True:
    n = float(input())

    if n >= 0 and n <= 10:
        count += 1
        sum += n

    else:
        print("nota invalida")

    if count == 2:
        break

print("media = %.2f" % (sum / 2.0))
