# from typing import List

# class Solution:
#     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
       
#         subarrays = []
#         count = 0
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums) + 1):
#                 subarrays.append(nums[i:j])

#         for ar in subarrays:
#             if sum(ar) == goal:
#                 count += 1

#         return count
    

# s = Solution()
# print(s.numSubarraysWithSum(nums = [1,0,1,0,1], goal = 2))

################### Memory errors #################