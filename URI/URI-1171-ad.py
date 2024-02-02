from collections import Counter

n = int(input())
li = []
for i in range(n):
    a = int(input())
    li.append(a)

d = Counter(li)
d = dict(sorted(d.items()))
           
for key, value in d.items():
    print("{} aparece {} vez(es)".format(key, value))
