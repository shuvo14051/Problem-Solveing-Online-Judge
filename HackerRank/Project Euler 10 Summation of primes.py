test = int(input())
for i in range(test):
    sum = 0
    number = int(input())
    for num in range(2, number):
        count = 0
        for j in range(2, num):
            if num % j == 0:
                count += 1
        if count == 0:
            sum += num

    print(sum)
