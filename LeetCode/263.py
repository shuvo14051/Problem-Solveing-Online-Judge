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
        if n<=0:
            return False
        if n == 1:
            return True
        factors = []
        prime_factors =[]
        for i in range(2, n):
            if n%i == 0:
                factors.append(i)
        
        for i in factors:
            if self.is_prime(i):
                prime_factors.append(i)
                
        if not prime_factors:
            return False
        
        if 2 in prime_factors:
            prime_factors.remove(2)
        if 3 in prime_factors:
            prime_factors.remove(3)
        if 5 in prime_factors:
            prime_factors.remove(5)

        if prime_factors:
            return False
        return True

        
    
s = Solution()

print(s.isUgly(1))
        