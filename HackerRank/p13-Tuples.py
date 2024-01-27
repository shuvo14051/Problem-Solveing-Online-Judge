n = int(input())

ar = list(map(int,input().split())) [:n]

li = []

for i in ar:
    li.append(i)

t = tuple(li)

print(hash(t))
