from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minimum = nums[0]
        for num in nums:
            if abs(num) < abs(minimum):
                minimum = num

        if minimum < 0 and abs(minimum) in nums:
            return abs(minimum)
        else:
            return minimum
