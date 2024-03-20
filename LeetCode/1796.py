from collections import Counter

class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set(c for c in s if c.isdigit())
        result = sorted(list(digits))[-2] if len(digits) > 1 else -1
        return int(result)
    
s = Solution()
print(s.secondHighest("ck077"))