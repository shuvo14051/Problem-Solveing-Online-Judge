class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        summ = 0
        for i in s:
            diff = abs(s.index(i) - t.index(i))
            summ+=diff

        return summ
    
s = Solution()
print(s.findPermutationDifference(s = "abc", t = "bac"))