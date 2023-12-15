n = int(input())

ar = list(map(int, input().split()))

count = 0

for i in ar:
    if i == 1:
        count += 1

print(count)