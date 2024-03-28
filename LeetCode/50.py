import math

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return math.pow(x, n)
    

s = Solution()
print(s.myPow(2,-2))