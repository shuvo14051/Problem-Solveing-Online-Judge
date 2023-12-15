n = int(input())

for i in range(1, n + 1):
    square = i * i
    cube = i * i * i
    print("{0} {1} {2}".format(i, square, cube))
    print("{0} {1} {2}".format(i, square + 1, cube + 1))
