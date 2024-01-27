# Print the header
print("---------------------------------------")
print("| decimal   |  octal  |  Hexadecimal  |")
print("---------------------------------------")

# Print the table content using a loop
for decimal in range(16):
    octal = oct(decimal)[2:]
    hexadecimal = hex(decimal)[2:].upper()
    print("|{:^11}|{:^9}|{:^15}|".format(decimal, octal, hexadecimal))

# Print the footer
print("---------------------------------------")
