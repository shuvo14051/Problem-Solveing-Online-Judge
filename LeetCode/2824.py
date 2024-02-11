from typing import List
import itertools

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs = itertools.combinations(nums, 2)
        count = 0
        for pair in pairs:
            if  pair[0] + pair[1] < target:
                count += 1
            
        return count
    
s = Solution()
print(s.countPairs([-1,1,2,3,1], 2))