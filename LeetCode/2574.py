from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum  = []
        rightSum = []
        for i in range(len(nums)):
            leftSum.append(sum(nums[0:i]))
        nums.reverse()
        for i in range(len(nums)):
            rightSum.append(sum(nums[0:i]))
        rightSum.reverse()

        result = []
        for i in range(len(nums)):
            diff = leftSum[i] - rightSum[i]
            result.append(abs(diff))

        return result
    
    
s = Solution()
print(s.leftRightDifference([10,4,8,3]))
