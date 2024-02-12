class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s = str(num)
        rev1 = int(s[::-1])
        rev2 = str(rev1)[::-1]

        return num == int(rev2)
    
s = Solution()
print(s.isSameAfterReversals(526))