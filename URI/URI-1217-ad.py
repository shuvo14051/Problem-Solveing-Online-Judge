n = int(input())
kgs = []
for i in range(n):
    amount = float(input())
    li = list(map(int, input().split()))
    kgs.append(len(li))
