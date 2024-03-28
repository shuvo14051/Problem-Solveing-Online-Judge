# from typing import List 

# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         sub = []
#         count = 0
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)+1):
#                 sub.append(nums[i:j])

#         for arr in sub:
#             mul = 1
#             for val in arr:
#                 mul*=val
#             if mul < k:
#                 count += 1
#         return count
    
# s = Solution()
# print(s.numSubarrayProductLessThanK([10,5,2,6],0))