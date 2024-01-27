n = int(input())

li = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    li[i] = list(map(int, input().split()))

li = list(map(list, zip(*li)))

count = 0
for i in li:
    if sum(i) == 0:
        count += 1

if count < 3:
    print("NO")
elif count == 3:
    print("YES")
