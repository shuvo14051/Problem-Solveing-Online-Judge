line1 = input()
line2 = input()

result = ""

for i in range(len(line1)):
    if line1[i] == line2[i]:
        result += "0"
    else:
        result += "1"

print(result)