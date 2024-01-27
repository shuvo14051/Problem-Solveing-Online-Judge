n = int(input())

while True:
    n += 1
    li = list(str(n))
    unique_li = set(li)
    
    if len(unique_li) == 4:
        print("".join(li))
        break