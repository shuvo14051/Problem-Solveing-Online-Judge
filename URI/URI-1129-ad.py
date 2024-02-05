
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        li = list(map(int, input().split()))
        count = 0
        for i in li:
            if i <= 127:
                count += 1
        if count > 1 or count == 0:
            print("*")
        if count == 1:
            result = li.index(min(li))
            if result == 0:
                print("A")
            elif result == 1:
                print("B")
            elif result == 2:
                print("C")
            elif result == 3:
                print("D")
            elif result == 4:
                print("E")