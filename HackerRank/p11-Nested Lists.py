ar = [[0 for j in range(2)] for i in range(5)]

marks = []

for i in range(5):
    for j in range(2):
        k = input()
        ar[i][j] = k

dic = {}

for i in ar:
    dic[float(i[1])] = i[0]

for i in dic.keys():
    marks.append(i)


print(marks)

