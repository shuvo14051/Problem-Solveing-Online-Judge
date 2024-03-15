import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        res = str(dividend / divisor)
        li = res.split(".")
        result = int(li[0])
        if result > 2147483647:
            return 2147483647
        return result

s = Solution()
print(s.divide(dividend = 7, divisor = -3))