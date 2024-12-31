class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(x) ** 2 for x in str(n))
            
        return n == 1
    
s = Solution()
print(s.isHappy(19))