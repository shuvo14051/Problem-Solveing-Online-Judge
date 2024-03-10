while True:
    a, b = input().split()
    if a == "0" and b == "0":
        break
    b = b.replace(a,"")
    if b == "":
        print(0)
    else:
        print(int(b))
