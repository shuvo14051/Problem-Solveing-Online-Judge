import math
class Solution:
    def mySqrt(self, x: int) -> int:
        s = math.sqrt(x)
        s = math.floor(s)

        return s
    

s = Solution()
print(s.mySqrt(8))