print("MUITO OBRIGADO")

alc = 0
gas = 0
dis = 0

while True:
    n = int(input())
    if n== 1:
        alc += 1
    elif n==2:
        gas +=1
    elif n == 3:
        dis += 1
    elif n ==4:
        break

print("Alcool: %d" %alc)
print("Gasolina: %d" %gas)
print("Diesel: %d" %dis)