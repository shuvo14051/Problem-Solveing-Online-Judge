n = int(input())

li = list(map(int, input().split()))

maxi = max(li)

summ = 0

for i in li:
    summ += (maxi-i)

print(summ)
