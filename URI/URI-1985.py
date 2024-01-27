n = int(input())
total = 0

for _ in range(n):
    code, quantity = input().split()
    quantity = float(quantity)
    if code == "1001":
        total += 1.5*quantity
    elif code == "1002":
        total += 2.5*quantity
    elif code == "1003":
        total += 3.5*quantity
    elif code == "1004":
        total += 4.5*quantity
    elif code == "1005":
        total += 5.5*quantity


print("{:.2f}".format(total))
