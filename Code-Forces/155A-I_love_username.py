n = int(input())
heights = list(map(int, input().split()))

max_height = 0
count = 0

for height in heights:
    if height > max_height:
        count += 1
        max_height = height

print(count)
