# from typing import List 
# from itertools import permutations

# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         perm = list(permutations(sorted(nums)))
#         index_of_nums = perm.index(tuple(nums))
#         if index_of_nums == len(perm)-1:
#             nums[:] = perm[0]
#         else:
#             nums[:] = perm[index_of_nums+1]

#         print(nums)
#         print(perm)

# s = Solution()
# s.nextPermutation([1,5,1])