from collections import Counter

n = int(input())
playlist = list(map(int, input().split()))
result = 0
counter = Counter(playlist)
m = max(counter.values())
for key, value in counter.items():
    if value == m:
        result+=1
print((result))
