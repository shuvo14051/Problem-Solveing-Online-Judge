n = int(input())
dic = {}
for i in range(n):
    a, b = input().split()
    dic[a] = b

for j in range(n):
    name = input()
    if name in dic:
        print("{}={}".format(name, dic[name]))
    else:
        print("Not found")
