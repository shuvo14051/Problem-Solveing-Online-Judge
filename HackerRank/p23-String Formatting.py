def print_formatted(n):
    for i in range(1, n + 1):

        li_oct = []
        final_oct = ''
        octal = oct(i)
        str_octal = str(octal)
        for j in str_octal[2:]:
            li_oct.append(j)
        for k in li_oct:
            final_oct += k

        li_hex = []
        final_hex = ''
        hexa = hex(i)
        str_hexa = str(hexa)
        for j in str_hexa[2:]:
            li_hex.append(j)
        for k in li_hex:
            final_hex += k.capitalize()

        li_bin = []
        final_bin = ''
        binary = bin(i)
        str_binary = str(binary)
        for j in str_binary[2:]:
            li_bin.append(j)
        for k in li_bin:
            final_hex += k

        print("{0} {1:4} {2:4} {3:8}".format(i, final_oct, final_hex, final_bin))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
