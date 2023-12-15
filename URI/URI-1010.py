code, unit, price = input().split()
code2, unit2, price2 = input().split()

code = int(code)
unit = int(unit)
price = float(price)

code2 = int(code2)
unit2 = int(unit2)
price2 = float(price2)

total = (unit*price) + (unit2*price2)

print("VALOR A PAGAR: R$ %.2f" %total)




