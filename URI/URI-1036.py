import math

a, b, c = input().split()
a, b, c = float(a), float(b), float(c)
x = ((b * b) - (4 * a * c))

if (a == 0 or x < 0):
    print("Impossivel calcular")

else:
    R1 = (-b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    R2 = (-b - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    print("R1 = %.5f" %R1)
    print("R2 = %.5f" %R2)

