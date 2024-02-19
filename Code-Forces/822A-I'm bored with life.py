# import math

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# a, b = map(int, input().split())

# fact_a = factorial(a)
# fact_b = factorial(b)
# gcd = math.gcd(fact_a, fact_b)
# print(gcd)


import math

n, m = map(int, input().split())
x = min(n, m)

k = 1
while x > 0:
    k *= x
    x -= 1

print(k)
