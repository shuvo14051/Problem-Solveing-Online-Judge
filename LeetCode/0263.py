class Solution:
    def is_prime(self, n):
        count = 0
        for i in range(2, n):
            if n%i == 0:
                count += 1
        if count == 0:
            return True
        return False
    
    def isUgly(self, n: int) -> bool:
        factors = []
        remove_track = 0
        if n <= 0:
            return False
        if n == 1:
            return True
        for i in range(2, n):
            if n%i == 0 and self.is_prime(i):
                factors.append(i)
        # if len(factors) == 0:
        #     return False
        # print("All prime factors: ", factors)
        if 2 in factors:
            factors.remove(2)
            remove_track += 1
        if 3 in factors:
            factors.remove(3)
            remove_track += 1
        if 5 in factors:
            factors.remove(5)
            remove_track += 1

        # print("After removal: ", factors)
        # print(remove_track)
        if len(factors) == 0 and remove_track>=1:
            return True
        return False
    
s = Solution()

print(s.isUgly(6))
        