t = int(input())

for i in range(t):
    coin1, coin2 = 0, 0
    n = int(input())
    # 1x + 2x = n
    # so I need to find the value of x
   
    coin1 = n//3
    coin2 = coin1

    fraction = n/3 - coin1
    
    if  fraction >= 0.5:
        coin2 += 1
    elif  fraction > 0 and fraction < 0.5:
        coin1 += 1

    print(coin1, coin2)