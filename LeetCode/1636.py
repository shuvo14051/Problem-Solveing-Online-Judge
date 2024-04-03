# Wrong answer

# from typing import List
# from collections import Counter

# class Solution:
#     def frequencySort(self, nums: List[int]) -> List[int]:
#         li = []
#         counter = Counter(nums)
#         counter = dict(sorted(counter.items(), key=lambda x: x[1]))
#         for key, val in counter.items():
#             li.extend([key]*val)
#         return li
    
# s = Solution()
# print(s.frequencySort(nums = [1,1,2,2,2,3]))