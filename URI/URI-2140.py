price, paid = map(int, input().split())
base = [100, 50, 30, 10, 5 , 2]
change = paid - price
while change != 0:
    