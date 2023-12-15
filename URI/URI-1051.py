salary = float(input())
tax = 0
if salary <= 2000:
    print("Isento")

else:
    taxable_salary = salary - 2000.00
    print("taxable salary:", taxable_salary)

    if salary >= 2000.01 and salary <= 3000.00:
        tax = taxable_salary * .08
        print("block 1")

    elif salary >= 3000.01 and salary <= 4500.00:
        tax = taxable_salary * .18
        print("block 2")


    elif salary > 4500.0:
        tax = taxable_salary * .28
        print("block 3")

    print(tax)
