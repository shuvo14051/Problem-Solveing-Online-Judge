t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    result = ""
    for i in range(a,b+1):
        result += str(i)
    for i in range(b,a-1,-1):
        i = str(i)
        result += (i[::-1])

    print(result)