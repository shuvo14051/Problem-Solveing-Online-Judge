li = []
for i in range(100):
    n = float(input())
    li.append(n)

index = 0

for i in li:
    if i <= 10:
        print("A[%d] = %.1f" %(index,i))
    index += 1