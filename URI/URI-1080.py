li = []
for i in range(100):
    n = int(input())
    li.append(n)


max = max(li)
result = li.index(max) + 1
print(max)
print(result)
