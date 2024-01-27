n = int(input())

width = len(bin(n)[2:])

for i in range(1, n+1):
    decimal = i
    octal = oct(i)
    hexa = hex(i)
    binary = bin(i)
    
    decimal = str(decimal)
    octal = str(octal)[2:]
    hexa = str(hexa)[2:].upper()
    binary = str(binary)[2:]

    print(decimal.rjust(width),octal.rjust(width),hexa.rjust(width),binary.rjust(width))