"""
Hash technique O(n)
"""

    

# class Solution:
#     def twoSum(self, nums, target):
#         for i in nums:
#             for j in nums[1:]:
#                 if i+j == target and i == j:
#                     return [nums.index(i), nums.index(j, nums.index(i)+1)]
#                 elif i+j == target:
#                     return [nums.index(i), nums.index(j)]

# 2nd apparoach
# class Solution(object):
#   def twoSum(self, nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
 
                

s = Solution()
print(s.twoSum(nums = [2,7,11,15], target = 9))