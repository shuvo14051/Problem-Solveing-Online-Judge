from typing import List 

# Complexity is O(n)
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
"""

# Complexity is O(log n)
class Solution:

    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
        
            else:
                right = mid
                
        return nums[left]
