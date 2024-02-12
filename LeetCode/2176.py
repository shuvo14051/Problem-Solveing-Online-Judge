from typing import List
from itertools import combinations

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        pairs = list(combinations(nums, 2))
        print(pairs)
        for pair in pairs:
            if pair[0] == pair[1]:
                count += 1

        return count
    
s = Solution()
print(s.countPairs(nums = [3,1,2,2,2,1,3], k = 2))