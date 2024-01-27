n, h = map(int, input().split())
li = list(map(int, input().split()))[:n]
width = 0

for i in li:
    if i >  h:
        width += 2
    else:
        width += 1

print(width)