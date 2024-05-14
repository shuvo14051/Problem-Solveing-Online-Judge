n = int(input())
dic = {}
for i in range(n):
    a, b = input().split()
    dic[a] = b

# Did not use the try except block and a run time error occurred
for j in range(n):
    try:
        name = input()
        if name in dic:
            print("{}={}".format(name, dic[name]))
        else:
            print("Not found")
    except:
        break
