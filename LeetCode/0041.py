from typing import List

class Solution:
    def firstMissingPositive(self, nums):
        num_set = set(nums)
        positive_number = 1
        while positive_number in num_set:
            positive_number += 1
        return positive_number
            

s = Solution()
print(s.firstMissingPositive([1]))