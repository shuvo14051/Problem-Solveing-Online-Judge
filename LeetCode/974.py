from typing import List 

# Complexity is O(n^2). and time limit exceeded
"""
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        subarrays = []
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                subarrays.append(nums[i:j])

        for ar in subarrays:
            if sum(ar) % k == 0:
                count += 1
        return count
"""

# s = Solution()
# print(s.subarraysDivByK(nums = [5], k = 9))