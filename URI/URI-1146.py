while True:
    n = int(input())
    if n == 0:
        break
    for i in range(1,n):
        print(i, end=' ')

    # this line is to prevent the presentation error
    # we print from 1 to n-1 with a space after every number
    # and finally print n without any space after this
    print(n)
