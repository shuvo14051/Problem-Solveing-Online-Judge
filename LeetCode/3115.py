from typing import List 

class Solution:
    def isPrime(self, n: int) -> bool:
        if n < 2:
            return False  
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False 
        return True  

    def maximumPrimeDifference(self, nums: List[int]) -> int:
        primes = []
        for idx, num in enumerate(nums):
            if self.isPrime(num):
                primes.append(idx)
        return max(primes) - min(primes)
    

s = Solution()
print(s.maximumPrimeDifference([4,2,9,5,3]))