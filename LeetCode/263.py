


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        return n == 1
    
s = Solution()
print(s.isUgly(2))


# time limit
# class Solution:
#     def is_prime(self, n):
#         count = 0
#         for i in range(2, n):
#             if n%i == 0:
#                 count += 1
#         if count == 0:
#             return True
#         return False
    
#     def isUgly(self, n: int) -> bool:
#         if n<=0:
#             return False
#         if n == 1 or n==2:
#             return True
#         prime_factors =[]
#         for i in range(2, n+1):
#             if n%i == 0 and self.is_prime(i):
#                 prime_factors.append(i)

#         # print(prime_factors)
#         if len(prime_factors) == 0:
#             return False
#         else:
#             for i in prime_factors:
#                 if i not in [2,3,5]:
#                     return False
            
#         return True

# s = Solution()
# print(s.isUgly(2))