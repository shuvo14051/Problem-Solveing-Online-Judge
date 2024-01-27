n = int(input())

mishka = 0
chris = 0

for i in range(n):
    mis, ch = map(int, input().split())
    if mis > ch:
        mishka += 1
    elif mis < ch:
        chris += 1

if mishka > chris:
    print("Mishka")
elif chris > mishka:
    print("Chris")
elif mishka == chris:
    print("Friendship is magic!^^")