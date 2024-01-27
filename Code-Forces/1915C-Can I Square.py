import math

test = int(input())

for _ in range(test):
    n = int(input())
    li = list(map(int, input().split()))[:n]
    summ = sum(li)
    square = math.sqrt(summ)
    str_square = str(square)
    li_str = str_square.split(".")
    if li_str[-1] == '0':
        print("YES")
    else:
        print("NO")
    