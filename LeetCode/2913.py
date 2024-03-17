from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        length = len(nums)
        s = 0
        for i in range(length):
            for j in range(i+1, length+1):
                set_li = set(nums[i:j])
                s += len(set_li)**2
        return s
    
s = Solution()
print(s.sumCounts([1,2,1]))

