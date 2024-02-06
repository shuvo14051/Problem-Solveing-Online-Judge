test = int(input())

for i in range(test):
    a, b, c, d = map(int, input().split())
    # check a,b 
    first = a>c and a>d and b>c and b>d
    #check c,d
    second = c>a and c>b and d>a and d>b
    if first or second:
        print("NO")
    else:
        print("YES")