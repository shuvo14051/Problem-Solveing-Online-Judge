# approach 01 time limit exceeded
# test = int(input())

# for _ in range(test):
#     a, b = map(int, input().split())

#     divisors_a = set()
#     divisors_b = set()

#     for i in range(2, a+1):
#         if a%i == 0:
#             divisors_a.add(i)
#     for j in range(2, b+1):
#         if b%j == 0:
#             divisors_b.add(j)

#     li = list(divisors_a.intersection(divisors_b))
#     print(li)

# Approach 2 has the same problem
# test = int(input())

# for _ in range(test):
#     a, b = map(int, input().split())

#     max_common_divisor = 1

#     for i in range(2, min(a, b) + 1):
#         if a % i == 0 and b % i == 0:
#             max_common_divisor = i

#     print(max_common_divisor)

#  this worked
import math

def find_gcd(a, b):
    while b:
        a, b = b, a % b
        print("a",a)
        print("b",b)
    return a

test = int(input())

for _ in range(test):
    a, b = map(int, input().split())
    gcd = find_gcd(a, b)
    print(gcd)
