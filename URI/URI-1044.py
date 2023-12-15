x, y = map(int, input().split())

if x > y:
    # a pythonic way to swap
    # x, y = y, x
    c = x
    x = y
    y = c

if y%x == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")