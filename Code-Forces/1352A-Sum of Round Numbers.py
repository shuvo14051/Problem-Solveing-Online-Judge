test = int(input())
li = [1,2,3,4,5,6,7,8,9]
for _ in range(test):
    result = []
    n = int(input())
    tem = n
    if False:
        pass    
    else:
        while tem % 10 != 0:
            tem = tem - 1
            if tem % 10 == 0:
                result.append(tem)
            n = n //tem
            
            if n in li:
                result.append(li[n])

    print(result)
            
            
