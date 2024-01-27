x1, v1, x2, v2 = map(int, input().split())
d1 = x1+v1
d2 = x2+v2
c1 = 0
c2 = 0

if x2 > x1 and v2 > v1:
    print("No")

else:
    while d1 != d2:
        d1 += v1
        d2 += v2
        print(d1,d2)
