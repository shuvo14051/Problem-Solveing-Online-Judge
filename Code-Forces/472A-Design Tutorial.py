n = int(input())
li = []
for i in range(4, n):
    has_divisors = False
    for j in range(2, i):
        if i % j == 0:
            li.append(i)
            break  
    if len(li) == 2:
        break
print(li)