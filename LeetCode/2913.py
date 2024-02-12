from typing import List
from itertools import combinations
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        li = []
        s = 0
        for i in range(1,len(nums)+1):
            li.extend(combinations(nums, i))
        
        print(li)

        for j in li:
            length = len(set(j))
            s += length **2

        return s
    
s = Solution()
print(s.sumCounts([1,1]))

