ar1 = list(map(int,input().split()[:3]))
ar2 = list(map(int,input().split()[:3]))

a = 0
b = 0

if ar1[0] > ar2[0]:
    a += 1
elif ar1[0] < ar2[0]:
    b += 1

if ar1[1] > ar2[1]:
    a += 1
elif ar1[1] < ar2[1]:
    b += 1

if ar1[2] > ar2[2]:
    a += 1
elif ar1[2] < ar2[2]:
    b += 1

print(a,b)