from typing import List 

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                result.append(nums[i+1])
            else:
                result.append(-1)
        if nums[-2] > nums[-1]:
            result.append(nums[-2])
        else:
            result.append(-1)

        return result
    
    
s = Solution()
print(s.nextGreaterElements([1,2,1]))
print(s.nextGreaterElements([1,2,3,4,3]))
print(s.nextGreaterElements([5,4,3,2,1]))
