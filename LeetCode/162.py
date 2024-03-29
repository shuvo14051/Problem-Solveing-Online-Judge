from typing import List 
# Run time error
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i

s = Solution()
print(s.findPeakElement([1,2,3,1]))