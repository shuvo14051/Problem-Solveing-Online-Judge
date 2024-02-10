from collections import Counter

test = int(input())

for i in range(test):
    n = int(input())
    li = map(int, input().split())
    if n<3:
        print(-1)
    else:
        counter = Counter(li)
        for key, value in counter.items():
            if value >= 3:
                print(key)
                break
            else:
                print(-1)
