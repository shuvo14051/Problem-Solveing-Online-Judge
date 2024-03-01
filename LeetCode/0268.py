# first approach

# from typing import List

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         length = len(nums)
#         for i in range(length+1):
#             if i not in nums:
#                 return i

# s = Solution()
# print(s.missingNumber([0,1]))

# second approach
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
        
        actual_sum = sum(nums)  # Sum of elements in the list
        return expected_sum - actual_sum
