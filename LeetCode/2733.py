from typing import List 

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        maximum = max(nums)
        minimum = min(nums)
        for i in nums:
            if (i == maximum or i == minimum):
                if nums:
                    nums.remove(maximum)
                if nums:
                    nums.remove(minimum)

        if len(nums) == 0:
            return -1
        return nums[0]