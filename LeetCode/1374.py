import random

class Solution:
    def generateTheString(self, n: int) -> str:
        base = "ab"
        output = ""
        if n%2 == 0:
            output = base[0]*(n-1) + base[1]
        else:
            output = base[0]*n

        return output
    
s = Solution()
print(s.generateTheString(7))