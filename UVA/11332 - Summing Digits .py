try:
    while True:
        n = int(input())
        if n == 0:
            break
        if n<10:
            print(n)
        if n>9:
            while n>9:
                result = 0
                while n>0:
                    result = result + n%10
                    n = n//10
                n = result
            print(result)
except EOFError:
    pass