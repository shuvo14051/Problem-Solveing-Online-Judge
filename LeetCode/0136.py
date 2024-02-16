from typing import List 

# this beat 8% 
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         for i in nums:
#             if nums.count(i) == 1:
#                 return i


# this beat 78%
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for key, value in counter.items():
            if value == 1:
                return key