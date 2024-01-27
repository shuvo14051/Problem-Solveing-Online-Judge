a,b = [int(i) for i in input().split()]

if a == 1:
    total = 4.0*b

elif a == 2:
    total = 4.5*b

elif a == 3:
    total = 5.0*b

elif a == 4:
    total = 2.0*b

elif a == 5:
    total = 1.5*b


print("Total: R$ %.2f" %total)