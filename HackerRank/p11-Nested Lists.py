n = int(input())

d = {}

for i in range(n):
    name = input()
    score = float(input())
    d[name] = score
d = dict(sorted(d.items()))
values = [i for i in d.values() if i != min(d.values())]
minimum = min(values)

for key, value in d.items():
    if value == minimum:
        print(key)