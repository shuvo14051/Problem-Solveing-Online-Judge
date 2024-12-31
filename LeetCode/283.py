from typing import List

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         non_zero_index = 0  

#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
#                 non_zero_index += 1  

#         print(nums)

"""
Two pointer solution
"""
class Solution:
    def moveZeroes(self, nums):
        L = 0
        R = 1
        n = len(nums)
        while(R<n):
            if nums[L]!=0:
                L+=1
                R+=1
            elif nums[R] == 0:
                R+=1
            else:
                nums[L], nums[R] = nums[R], nums[L]

        return nums

s = Solution()
print(s.moveZeroes([0,1,0,3,12]))