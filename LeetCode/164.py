from typing import List 

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        nums = sorted(nums)
        ar = []
        for i in range(1, len(nums)):
            ar.append(abs(nums[i-1] - nums[i]))

        m = max(ar)
        return m
    
s = Solution()
print(s.maximumGap([3,6,9,1]))