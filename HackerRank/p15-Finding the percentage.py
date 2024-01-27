n = int(input())
dic = {}
total = 0
for i in range(n):
    ar = list(input().split()) [:4]
    key = ar[0]
    ar.pop(0)

    dic[key] = ar

name = input()

for i in dic.keys():
    if i == name:
        marks = dic[name]

for i in marks:
    total += float(i)

avg = total/3


print("%.2f" %avg)



