a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

triangle = .5 * a * c
circle = 3.14159 * c * c
trapezium = .5 * (a + b) * c
square = b*b
rectangle = a*b

print("TRIANGULO: %.3f" % triangle)
print("CIRCULO: %.3f" % circle)
print("TRAPEZIO: %.3f" % trapezium)
print("QUADRADO: %.3f" % square)
print("RETANGULO: %.3f" % rectangle)

