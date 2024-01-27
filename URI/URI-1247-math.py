while True:
    try:
        d, theif, police = map(int, input().split())
        if (d/theif) >= (d/police):
            print('S')
        else:
            print('N')

    except EOFError:
        break  