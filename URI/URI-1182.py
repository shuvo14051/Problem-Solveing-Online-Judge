line = int(input())
operation = input()

ar = [[0 for _ in range(12)] for _ in range(12)]

for i in range(12):
    for j in range(12):
        ar[i][j] = float(input())

column = [row[0] for row in ar]

if operation == "S":
    summ = sum(column)
    print("{:.1f}".format(summ))
elif operation == "M":
    avg = sum(column) / 12
    print("{:.1f}".format(avg))