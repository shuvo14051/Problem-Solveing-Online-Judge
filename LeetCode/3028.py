from typing import List 

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count = 0
        s = 0
        for i in nums:
            s += i
            if s == 0:
                count += 1

        return count