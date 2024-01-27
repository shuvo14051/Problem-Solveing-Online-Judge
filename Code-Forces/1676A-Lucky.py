test = int(input())

for _ in range(test):
    sum1, sum2 = 0, 0
    digit = input()

    first_half = digit[:3]
    second_half = digit[3:]

    for i in range(3):
        sum1 = sum1 + int(first_half[i])
        sum2 = sum2 + int(second_half[i])
    
    if sum1 == sum2:
        print("YES")
    else:
        print("NO")
