# from typing import List 


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         length = len(nums)
#         output = []
#         for i in nums:
#             mul = 1
#             for j in nums:
#                 if i == j:
#                     mul *= 1
#                 else:
#                     mul *= j
#             output.append(mul)
#         return output
    
# s = Solution()
# print(s.productExceptSelf(nums = [1,2,3,4]))
