n = int(input())
odd = []
even = []

for _ in range(n):
    k = int(input())
    if k%2 == 0:
        even.append(k)
    else:
        odd.append(k)

result = sorted(even) + sorted(odd, reverse=True)
for _ in result:
    print(_)