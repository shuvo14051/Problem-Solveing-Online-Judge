from typing import List
import itertools

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        m, conver = 0, []
        for x in nums:
            m = max(m, x)
            conver.append(x + m)
        return list(itertools.accumulate(conver))

# Test the function
s = Solution()
print(s.findPrefixScore([2, 3, 7, 5, 10]))
