# from typing import List

# class Solution:
#     def findMatrix(self, nums: List[int]) -> List[List[int]]:

#         nums_copy = nums[:]  # Create a copy of the input list
#         ar_2D = []

#         while nums:
#             li = []
#             for num in nums:
#                 print(nums)
#                 if num in li:
#                     # print("if block", num)
#                     continue
#                 elif num not in li:
#                     # print("elif block", num)
#                     li.append(num)
#                     nums.remove(num)
                
#             ar_2D.append(li)
#         return ar_2D

# s = Solution()
# print(s.findMatrix([1,2,3,4]))
