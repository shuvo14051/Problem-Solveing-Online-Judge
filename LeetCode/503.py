# from typing import List 

# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         result = []
#         for i in range(len(nums)):
#             if nums[i] == max(nums):
#                 result.append(-1)
#             else:
#                 result.append(max(nums))
            
#         return result
    
    
# s = Solution()
# print(s.nextGreaterElements([1,2,1]))
# print(s.nextGreaterElements([1,2,3,4,3]))
# print(s.nextGreaterElements([5,4,3,2,1]))
