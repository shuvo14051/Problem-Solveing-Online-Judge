li = []
for i in range(10):
    n = int(input())
    li.append(n)

index = 0

for i in li:
    if i <= 0:
        i = 1
    print("X[%d] = %d" %(index,i))
    index += 1