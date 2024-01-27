from itertools import  permutations

a,b = list(input().split())

b = int(b)

li = (list(permutations(a,b)))
result_li = []

for i in li:
    s = ''
    s = s + i[0] + i[1]
    result_li.append(s)

for j in result_li:
    print(j)

print(len(result_li))
