# Certification-Problem Solving - p-01

n = int(input())
li = []
for i in range(n):
    name = input()
    li.append(name)

dic = {}

for i in li:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

sum = 0
for j in dic.values():
    sum += j

result = []
for name, num in dic.items():
    if (num / sum) * 100 >= 5.0:
        result.append(name)

result.sort()
for i in result:
    print(i)
