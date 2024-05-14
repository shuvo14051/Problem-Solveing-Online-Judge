import math

class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        for i in range(1, len(s)):
            result += abs(ord(s[i]) - ord(s[i-1]))

        return result
            
s = Solution()
print(s.scoreOfString("zaz"))