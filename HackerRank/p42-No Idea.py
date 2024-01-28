n, m = map(int,input().split())
li = list(map(int,input().split()))[:n]

A = set(map(int,input().split()))
B = set(map(int,input().split()))

result = 0

for i in li:
    if i in A:
        result += 1
    if i in B:
        result -= 1

print(result)

