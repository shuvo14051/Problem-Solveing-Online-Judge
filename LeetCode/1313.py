# from typing import List 

# class Solution:
#     def decompressRLElist(self, nums: List[int]) -> List[int]:
#         first_pair = nums[0:2]
#         secnd_pair = nums[2:]

#         li = []

#         li.extend([first_pair[1]]*first_pair[0])
#         li.extend([secnd_pair[1]]*secnd_pair[0])

#         return li
    
# s = Solution()
# print(s.decompressRLElist([1,1,2,3]))