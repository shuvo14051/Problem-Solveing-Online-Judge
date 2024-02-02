
while True:
    n = int(input())
    res = ""
    if n == 0:
        break
    li = []
    sorted_li = []
    for i in range(n):
        name = input()
        color, size = input().split()
        li.append(color + " " + size + " " + name)
    for i in sorted(li):
        i.split(" ")



