# from typing import List 
# from collections import Counter

# class Solution:
#     def maxSubarrayLength(self, nums: List[int], k: int) -> int:
#         start = len(nums)-1
#         for i in range(start,-1,-1):
#             counter = Counter(nums[:i+1])
#             occurance = list(counter.values())
#             if all(x <= k for x in occurance):
#                 return len(nums[:i+1])


# s = Solution()
# print(s.maxSubarrayLength(nums = [1,2,3,1,2,3,1,2], k = 2))

