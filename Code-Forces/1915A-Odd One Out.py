from collections import defaultdict

t = int(input())
for _ in range(t):
    li = list(map(int, input().split()))
    d = defaultdict(int)
    for i in li:
        d[i] += 1
    for key, value in d.items():
        if value == 1:
            print(key)
