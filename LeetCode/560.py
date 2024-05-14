from typing import *

# Did not solve yet
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      count = 0
      n = len(nums)
      pref = [0]*(n+1)
      for i in range(n):
         pref[i+1] = nums[i] + pref[i]
      return pref
    
s = Solution()
print(s.subarraySum(nums = [1,1,1], k = 2))


# Time limit
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      count = 0
      subarrays = []
      for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
          subarrays.append(nums[i:j])

      for i in subarrays:
        if sum(i) == k:
          count += 1
      return count
"""
