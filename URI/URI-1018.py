money = int(input())

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

m_1 = r5//1

print("%d" %money)
print("%d nota(s) de R$ 100,00" %m_100)
print("%d nota(s) de R$ 50,00" %m_50)
print("%d nota(s) de R$ 20,00" %m_20)
print("%d nota(s) de R$ 10,00" %m_10)
print("%d nota(s) de R$ 5,00" %m_5)
print("%d nota(s) de R$ 2,00" %m_2)
print("%d nota(s) de R$ 1,00" %m_1)


