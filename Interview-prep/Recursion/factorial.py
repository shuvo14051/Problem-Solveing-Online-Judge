"""Iterative approach"""
# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact * i

#     return fact

"""Recursive approach"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)

fact = factorial(5)
print(fact)