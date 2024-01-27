tea_type = int(input())
li = list(map(int, input().split()))
count = 0

for i in li:
    if i == tea_type:
        count += 1
print(count)