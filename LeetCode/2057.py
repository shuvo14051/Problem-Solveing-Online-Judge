from typing import List 

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            if idx % 10 == num:
                return idx
            
        return -1
    
s = Solution()
print(s.smallestEqual([4,3,2,1]))