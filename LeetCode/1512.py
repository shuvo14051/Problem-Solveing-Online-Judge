from typing import List
import itertools

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        pairs = itertools.combinations(nums, 2)
        for i in pairs:
            if i[0] == i[1]:
                count += 1

        return count
    

s = Solution()
print(s.numIdenticalPairs([1,1,1,1]))