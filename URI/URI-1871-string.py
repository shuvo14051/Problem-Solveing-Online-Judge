while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    s = str(a+b)
    if '0' in s:
        s = s.replace('0', '')
    print(s)
