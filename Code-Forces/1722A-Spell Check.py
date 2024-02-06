test = int(input())
base = ''.join(sorted("Timur"))

for i in range(test):
    n = int(input())
    name = input()
    name = ''.join(sorted(name))
    if len(name) != 5:
        print("NO")
    else:
        if name == base:
            print("YES")
        else:
            print("NO")