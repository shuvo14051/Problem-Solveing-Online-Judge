n = float(input())

if n >= 0 and n <= 400.0:
    total = n + (n * .15)
    increased_salary = total - n
    print("Novo salario: %.2f" % total)
    print("Reajuste ganho: %.2f" % increased_salary)
    print("Em percentual: 15 %")

elif n >= 400.01 and n <= 800.0:
    total = n + (n * .12)
    increased_salary = total - n
    print("Novo salario: %.2f" % total)
    print("Reajuste ganho: %.2f" % increased_salary)
    print("Em percentual: 12 %")

elif n >= 800.01 and n <= 1200.0:
    total = n + (n * .1)
    increased_salary = total - n
    print("Novo salario: %.2f" % total)
    print("Reajuste ganho: %.2f" % increased_salary)
    print("Em percentual: 10 %")

if n >= 1200.01 and n <= 2000.0:
    total = n + (n * .07)
    increased_salary = total - n
    print("Novo salario: %.2f" % total)
    print("Reajuste ganho: %.2f" % increased_salary)
    print("Em percentual: 7 %")

elif n > 2000:
    total = n + (n * .04)
    increased_salary = total - n
    print("Novo salario: %.2f" % total)
    print("Reajuste ganho: %.2f" % increased_salary)
    print("Em percentual: 4 %")
