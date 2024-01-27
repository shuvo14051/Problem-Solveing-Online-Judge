test = int(input())
for i in range(test):
    divisiors = []
    count = 0
    num = int(input())
    for i in range(2, num+1):
        count = 0
        if num % i == 0:
            print(i)
            for j in range(3, i+1):
                if i % j == 0:
                    count += 1
            if count == 0:
                divisiors.append(i)

    print(divisiors)
