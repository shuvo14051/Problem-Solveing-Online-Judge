from itertools import product

li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

result = list(product(li1, li2))
final = ''

for i in result:
    final = final+str(i) + ' '

print(final)
