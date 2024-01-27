test = int(input())
result = 0
for i in range(test):
    a,b = input().split()

    try:
        a = int(a)
        b = int(b)
        result = a//b
        print(result)

    except ZeroDivisionError as e:
        print("Error Code:", e)

    except ValueError as e:
        print("Error Code:" ,e)

