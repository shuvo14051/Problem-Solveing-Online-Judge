while True:
    try:
        n = int(input())
        res = ((n*(n+1))//2)**2
        print((res))

    except EOFError:
        break