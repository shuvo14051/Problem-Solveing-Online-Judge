# file = open('teste.txt', 'w')
# file = open('teste.txt', 'w')
check = 0
while True:
    n = int(input())
    if n == 0:
        break
    if check == 1:
        print()
        # file.write('\n')
    l = []
    for i in range(n):
        l.append(' '.join(input().split()))
    m = max(len(i) for i in l)

    for i in range(len(l)):
        for j in range(m-len(l[i])):
            print('', end=' ')
            # file.write(' ')
        print(l[i])
        # file.write(l[i])
        # file.write('\n')

    check = 1

#Presentation error
"""
while True:
    n = int(input())
    if n == 0:
        break
    li = []
    for i in range(n):
        line = input().strip()
        line = ' '.join(line.split())
        li.append(line)
    maximum = max(li, key=len)
    output = []
    for sen in li:
        space = len(maximum) - len(sen)
        sen = " "*space + sen
        print(sen)
    print()

"""