class Solution:
    def prime(self, num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    def countPrimes(self, n: int) -> int:
        li = []
        if n < 2:
            return 0
        for i in range(2, n):
            if self.prime(i):
                li.append(i)
        return len(li)
    
s = Solution()
print(s.countPrimes(10))
