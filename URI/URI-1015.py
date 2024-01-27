import  math

x1, y1 = [float(x) for x in input().split()]
x2, y2 = [float(x) for x in input().split()]

x = (x2-x1)**2
y = (y2-y1)**2

distance = math.sqrt(x+y)

print("%.4f" %distance)