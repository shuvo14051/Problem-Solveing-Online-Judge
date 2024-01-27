salary = float(input())
tax = 0
if salary <= 2000:
    print("Isento")

else:
    taxable_salary = salary - 2000.00

    if salary >= 2000.01 and salary <= 3000.00:
        # print("R$ %.2f\n"% (salary - 2000.00)*0.08)
        print("R$ {:.2f}".format((salary - 2000.00)*0.08))

    elif salary >= 3000.01 and salary <= 4500.00:
        print("R$ {:.2f}".format((salary - 3000.00)*0.18 + 1000.00*0.08))

        # print("R$ %.2f\n"% ((salary - 3000.00)*0.18 + 1000.00*0.08))

    elif salary > 4500.0:
        print("R$ {:.2f}".format((salary - 4500.00)*0.28 + 1500.00*0.18 + 1000.00*0.08))
        # print("R$ %.2f\n"% ((salary - 4500.00)*0.28 + 1500.00*0.18 + 1000.00*0.08))

