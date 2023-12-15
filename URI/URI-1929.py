li = list(map(int, input().split()))[:4]

i = 0

while True:
    li.pop(i)
    i += 1
    if (li[0] + li[1] > li[2]) or (li[0] + li[2] > li[1]) or (li[1] + li[2] > li[0]):
        print("Y")
        break
    else:
        print("N")
        break