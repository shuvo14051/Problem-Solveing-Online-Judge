from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        length = len(nums)
        s = 0
        for i in range(1, length+4):
            if length % i == 0:
                # this is because the given array was 1-indexed
                # but in python list is 0 indexed
                s += nums[i-1]**2

        return s
    
s = Solution()
print(s.sumOfSquares([2,7,1,19,18,3]))