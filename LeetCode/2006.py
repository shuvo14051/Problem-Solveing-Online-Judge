from typing import List
import itertools

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        pairs = itertools.combinations(nums, 2)
        count = 0
        # print(list(pairs))
        for pair in pairs:
            if abs(pair[0] - pair[1]) == k:
                count += 1
        return count
    
s = Solution()
print(s.countKDifference([3,2,1,5,4], 2))