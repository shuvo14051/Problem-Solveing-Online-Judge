x, y, z = map(float, input().split())

if (x+y > z) and (x+z > y) and (y+z > x):
    perimeter = x+y+z
    print("Perimetro = %.1f" %perimeter)

else:
    area = .5*(x+y)*z
    print("Area = %.1f" %area)