n = int(input())
c_id = []
j_id = []
for i in range(n):
    item = int(input())
    c_id.append(item)

k = int(input())
for i in range(n):
    item = int(input())
    j_id.append(item)

sum = 0
for i in c_id:
    min = 999
    for j in j_id:
        min_2 = j - i
        if min_2 < min and min_2 >= 0:
            min = min_2
    sum += min

    # print(sum)
print(sum)