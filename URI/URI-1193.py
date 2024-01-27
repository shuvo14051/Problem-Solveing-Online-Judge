test = int(input())
count = 1

for _ in range(test):
    n, text = input().split()
    if text == 'bin':
        deci =int(n, 2)
        hexa = hex(int(n, 2))[2:]

        print("Case {}:".format(count))
        print("{} dec".format(deci))
        print("{} hex".format(hexa))
        print()

    elif text == 'dec':
        bina = bin(int(n))[2:]
        hexa = hex(int(n))[2:]

        print("Case {}:".format(count))
        print("{} hex".format(hexa))
        print("{} bin".format(bina))
        print()

    elif text == 'hex':
        bina = bin(int(n, 16))[2:]
        deci = int(n, 16)
        print("Case {}:".format(count))
        print("{} dec".format(deci))
        print("{} bin".format(bina))
        print()

    count += 1