test = int(input())

for _ in range(test):
    name1, par1, name2, par2 = input().split()
    num1, num2 = map(int, input().split())
    summ = num1 + num2

    if summ%2==0:
        if par1 == 'PAR':
            print(name1)
        else:
            print(name2)
    elif summ%2!=0:
        if par2 == 'IMPAR':
            print(name2)
        else: 
            print(name1)