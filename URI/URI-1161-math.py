while True:
    try:
        a, b = map(int, input().split())

        def factorial(n):
            if n == 0:
                return 1
            return n*factorial(n-1)

        result = factorial(a) + factorial(b)

        print(result)
    except EOFError:
        break