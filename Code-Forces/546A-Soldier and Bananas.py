k, n, w = map(int, input().split())

total_cost = 0

for i in range(1,w+1):
    total_cost = total_cost + (k*i)

result = total_cost - n

if result <= 0:
    print(0)
else:
    print(result)
