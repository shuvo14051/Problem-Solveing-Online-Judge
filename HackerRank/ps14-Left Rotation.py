a,b = map(int, input().split())

li = list(map(int, input().split()))[:a]

for i in range(b):
    item = li.pop(0)
    li.append(item)

for i in li:
    print(i, end=' ')

