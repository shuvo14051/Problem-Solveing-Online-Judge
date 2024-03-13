i, r, k = map(int, input().split())

count = 0
for i in range(i, r+1):
    if i % k == 0:
        count += 1

print(count)