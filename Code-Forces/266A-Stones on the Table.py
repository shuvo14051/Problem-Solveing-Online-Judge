n = int(input())
stones = input()[:n]

count = 0
for i in range(0, len(stones)-1):
    if stones[i] == stones[i+1]:
        count += 1

print(count)
    