from typing import List

# Prefix sum O(n)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * (n+1)
        for i in range(n):
            pref[i+1] = nums[i] + pref[i]

        return pref[1:]
    
s = Solution()
print(s.runningSum([1,2,3,4]))

# Brute force  O(n^2)
"""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        li = []
        for i in range(len(nums)):
            li.append(sum(nums[0:i+1]))

        return li
"""