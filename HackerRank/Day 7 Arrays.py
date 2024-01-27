n = int(input())
li = list(map(int, input().split()))[:n]

li.reverse()
for i in li:
    print(i, end=' ')
