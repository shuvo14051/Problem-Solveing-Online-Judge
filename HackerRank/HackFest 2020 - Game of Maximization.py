n = int(input())
li = list(map(int, input().split()))[:n]

odd = []
even = []
sum1 = 0
sum2 = 0
result = 0

for i in range(0, len(li)):
    if i % 2:
        even.append(li[i])
    else:
        odd.append(li[i])

for i in even:
    sum1 = sum1 + i

for i in odd:
    sum2 = sum2 + i

while True:
    if sum1 == sum2:
        result = sum1 + sum2
        break
    elif sum1 > sum2:
        sum1 -= 1
    else:
        sum2 -= 1

print(result)
