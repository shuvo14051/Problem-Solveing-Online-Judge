from typing import List
from itertools import combinations

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        count = 0
        pairs = combinations(nums,2)
        for pair in pairs:
            pair_sum = pair[0] + pair[1]
            if lower <= pair_sum <= upper:
                count += 1

        return count
    
s = Solution()
print(s.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6))

