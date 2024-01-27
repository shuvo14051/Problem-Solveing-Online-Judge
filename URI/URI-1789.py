while True:
    try:
        n = int(input())
        numbers_str = input()
        numbers_list = [int(num) for num in numbers_str.split()][:n]

        speedy = max(numbers_list)

        if speedy < 10:
            print(1)
        elif speedy >=10 and speedy < 20:
            print(2)
        else:
            print(3)
    except EOFError:
        break
