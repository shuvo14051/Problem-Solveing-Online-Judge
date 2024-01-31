new_line = 0
while True:
    try:
        year = int(input())
        b = 0
        ord = 1
        if new_line:
            print('')
        new_line = 1

        if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
            print('This is leap year.')
            b = 1
            ord = 0
        if (year % 15 == 0):
            print('This is huluculu festival year.')
            ord = 0
        if (year % 55 == 0) and b:
            print('This is bulukulu festival year.')

        if ord:
            print('This is an ordinary year.')

    except EOFError:
        break
