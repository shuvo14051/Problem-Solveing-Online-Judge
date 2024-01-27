result = ""
maths = input()
li = list(map(int, maths.split('+')))
li.sort()
result = '+'.join(map(str, li))
print(result)