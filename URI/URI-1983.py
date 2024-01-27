n = int(input())
d = {}
result = ""

for _ in range(n):
    code, rating = input().split()
    d[code] = float(rating)

li = list(d.values())
maxi = max(li)

if maxi < 8:
    print("Minimum note not reached")
else:
    for key, value in d.items():
        if value == maxi:
            print(key)
