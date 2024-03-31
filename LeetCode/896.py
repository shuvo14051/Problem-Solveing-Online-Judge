from typing import List 

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True 
        for i in range(len(nums)-1):
            if (nums[i+1] < nums[i]):
                increasing = False
            if (nums[i+1] > nums[i]):
                decreasing = False

        return increasing or decreasing

s = Solution()
print(s.isMonotonic([1,2,4]))
