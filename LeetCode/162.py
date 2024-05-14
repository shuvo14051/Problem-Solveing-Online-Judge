from typing import List 

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak = 0
        if len(nums) <= 2:
            return nums.index(max(nums))
        else:
            for i in range(1, len(nums)-1):
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    peak = i
                    break
        return peak


s = Solution()
print(s.findPeakElement([1,2]))