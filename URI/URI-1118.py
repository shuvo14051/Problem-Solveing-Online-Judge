count = 0
sum = 0
while True:
    n = float(input())

    if n >= 0 and n <= 10:
        count += 1
        sum += n

    else:
        print("nota invalida")

    if count == 2:
        print("media = %.2f" % (sum / 2.0))
        print("novo calculo (1-sim 2-nao)")
        count = 0
        sum = 0
        option = int(input())

        if option == 2:
            break
        elif option == 1:
            continue
        else:
            print("novo calculo (1-sim 2-nao)")
            continue

