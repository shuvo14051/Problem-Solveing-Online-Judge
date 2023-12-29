while True:
    try:
        M, N = map(int,input().split())
    except EOFError:
        break
    
    # if M == 0 and N == 0:
    #     break
    li = []
    for i in range(M, N+1):
        count = 1
        while i!=1:
            if i%2 == 0:
                i = i//2
                count += 1
            elif i%2 != 0:
                i = (3*i+1)
                count += 1
        li.append(count)

    print(M, N, max(li))

