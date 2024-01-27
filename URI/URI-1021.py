money_total = float(input())
money = int(money_total)

moedas  = int(money_total*100)
print(moedas )

m_100 = money//100
r = money%100

m_50 = r//50
r1 = r%50

m_20 = r1//20
r2 = r1%20

m_10 = r2//10
r3 = r2%10

m_5 = r3//5
r4 = r3%5

m_2 = r4//2
r5 = r4%2

m1 = money // 1;
notas = money % 1;
m50 = moedas // 50;
moedas = moedas % 50;
m25 = moedas // 25;
moedas = moedas % 25;
m10 = moedas // 10;
moedas = moedas % 10;
m05 = moedas // 5;
moedas = moedas % 5;
m01 = moedas // 1;


print("NOTAS:")
print("%d nota(s) de R$ 100.00" %m_100)
print("%d nota(s) de R$ 50.00" %m_50)
print("%d nota(s) de R$ 20.00" %m_20)
print("%d nota(s) de R$ 10.00" %m_10)
print("%d nota(s) de R$ 5.00" %m_5)
print("%d nota(s) de R$ 2.00" %m_2)

print("MOEDAS:")

print("{} moeda(s) de R$ 1.00".format(m1))
print("{} moeda(s) de R$ 0.50".format(m50))
print("{} moeda(s) de R$ 0.25".format(m25))
print("{} moeda(s) de R$ 0.10".format(m10))
print("{} moeda(s) de R$ 0.05".format(m05))
print("{} moeda(s) de R$ 0.01".format(m01))


