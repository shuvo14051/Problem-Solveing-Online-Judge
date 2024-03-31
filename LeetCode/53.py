from typing import List 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]
        for i in nums[1:]:
            current_sum = max(i, i+current_sum)
            max_sum = max(max_sum, current_sum)

        return max_sum


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


# Brute force with O(n^2)
# Time limit exceeded
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                s.append(sum(nums[i:j]))

        return max(s)
"""
