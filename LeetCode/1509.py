# from typing import List 

# class Solution:
#     def minDifference(self, nums: List[int]) -> int:
#         m = min(nums)
#         numberOfMoves = 3
#         for i in range(numberOfMoves):
#             nums = sorted(nums)
#             nums[-1] = m

#         return max(nums) - min(nums)
    
# s = Solution()
# print(s.minDifference(nums = [1,5,0,10,14]))