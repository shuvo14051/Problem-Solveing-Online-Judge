n, k = map(int, input().split())
arr = list(map(int, input(). split()[:n]))

for i in range (k):
    poped_item = arr.pop(0)
    arr.append(poped_item)

for i in arr:
    print(i, end= ' ')