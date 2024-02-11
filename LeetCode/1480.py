from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        li = []
        for i in range(len(nums)):
            li.append(sum(nums[0:i+1]))

        return li

s = Solution()
print(s.runningSum([1,2,3,4]))