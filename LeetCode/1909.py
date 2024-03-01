from typing import List 

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)-1):
            if nums[i] >= nums[i+1]:
                nums.remove(nums[i])
                break
        print(nums)
        for j in range(0, len(nums)-1):
            if nums[j] >= nums[j+1]:
                return False
        return True
    
s = Solution()
print(s.canBeIncreasing([105,924,32,968]))