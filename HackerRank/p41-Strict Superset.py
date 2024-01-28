A = set(map(int, input().split()))
n = int(input())
result = None
for i in range(n):
    B = set(map(int, input().split()))
    if not B.issubset(A) or B == A:
        result = False
        break
else:
    result = True

print(result)