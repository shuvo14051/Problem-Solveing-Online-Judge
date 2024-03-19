from typing import List 


"""
nums =
[105,924,32,968]

Stdout
[105, 32, 968]

Output
false

Expected
true
"""
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            temp = nums[:i] + nums[i + 1:]
            if all(temp[j-1] < temp[j] for j in range(1, len(temp))):
                return True
        return False
    
s = Solution()
print(s.canBeIncreasing([105,924,32,968]))

"""
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] <= nums[i-1]:
                nums.pop(i)
                break
        print(nums)
        for j in range(0, len(nums) - 1):
            if nums[j] >= nums[j+1]:
                return False
        return True
        
"""