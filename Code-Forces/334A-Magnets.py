n = int(input())
li = []
for i in range(n):
    magnate = input()
    li.append(magnate)

first = li[0]
count = 0
for i in li:
    if len(li) == 2:
        count = 2
        break
    elif i != first:
        break
    count += 1

print(count)