n = int(input())

li = list(map(int, input().split()))[:n]

m = int(input())
sum = 0

for i in range(m):
    a,b = map(int, input().split())
    if a in li:
        li.remove(a)
        sum += b

print(sum)