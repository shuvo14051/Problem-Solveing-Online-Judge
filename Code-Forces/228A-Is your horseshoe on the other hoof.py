li = list(map(int, input().split()))[:4]

unique = set(li)

required = 4 - len(unique)

print(required)
