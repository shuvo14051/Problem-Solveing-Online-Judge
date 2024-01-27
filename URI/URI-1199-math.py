while True:
    n = input()
    if n == '-1':
        break
    if n[:2] == '0x':
        decimal_value = int(n, 16)
        print(decimal_value)
    else:
        hexa = hex(int(n))
        output = hexa[:2] + hexa[2:].upper()
        print(output)