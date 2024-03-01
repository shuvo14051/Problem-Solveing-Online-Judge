import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n - 1) == 0
    
s = Solution()
print(s.isPowerOfTwo(2))