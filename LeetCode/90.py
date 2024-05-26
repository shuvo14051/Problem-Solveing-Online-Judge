# from typing import List 
# from itertools import chain, combinations
# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         output = []
#         combi = list(chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1)))
#         for com in combi:
#             if list(com) not in output:
#                 output.append(list(com))

#         return output
# s = Solution()
# print(s.subsetsWithDup(nums = [1,2,3]))