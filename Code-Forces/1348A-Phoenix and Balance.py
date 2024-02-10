test = int(input())
for i in range(test):
    coins = int(input())
    left = 0
    right = 0
    li = [2**j for j in range(1, coins+1)]
    while li:
        if li:
            left += li.pop()
        if li:
            right += li.pop()
        li.reverse()

    print(left-right)

