li = []
for i in range(20):
    n = int(input())
    li.append(n)

li.reverse()

index = 0

for i in li:
    print("N[%d] = %d" %(index,i))
    index += 1