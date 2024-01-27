case = 1
while True:
    try:
        li = []
        n = int(input())
        for i in range(n+1):
            if i == 0:
                li.append(0)
            else:
                for j in range(i):
                    li.append(i)

            
        
        if len(li) == 1:
            print("Caso {}: {} numero".format(case, len(li)))
        else:
            print("Caso {}: {} numeros".format(case, len(li)))
        print(' '.join(str(num) for num in li))
        print()

        case += 1  
           

    except EOFError:
        break