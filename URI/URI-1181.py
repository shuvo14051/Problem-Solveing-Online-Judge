line = int(input())
operation = input()

ar = [[0 for _ in range(12)] for _ in range(12)]

for i in range(12):
    for j in range(12):
        ar[i][j] = float(input())

if operation == "S":
    summ = sum(ar[line])
    print("{:.1f}".format(summ))
elif operation == "M":
    avg = sum(ar[line]) / len(ar[line])
    print("{:.1f}".format(avg))