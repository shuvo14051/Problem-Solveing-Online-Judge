from typing import List 

# class Solution:
#     def minIncrementForUnique(self, nums: List[int]) -> int:
#         nums = sorted(nums)
#         count = 0
#         for i in range(1, len(nums)):
#             if nums[i-1] == nums[i]:
#                 count+=1
#                 nums[i] += 1
#             elif nums[i-1] > nums[i]:
#                 count+= nums[i-1] - nums[i] + 1
#                 nums[i] +=  (nums[i-1] - nums[i] + 1)

#         return count

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                count += increment
        return count
    
s = Solution()
print(s.minIncrementForUnique(nums = [3,2,1,2,1,7]))