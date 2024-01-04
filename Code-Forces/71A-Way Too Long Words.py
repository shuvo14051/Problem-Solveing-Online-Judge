n = int(input())

for i in range(n):
    res = ''
    line = input()
    if len(line)<=10:
        print(line)
    else:
        first = line[0]
        last = line[-1]
        length = len(line)-2
        res = first + str(length)+last
        print(res)