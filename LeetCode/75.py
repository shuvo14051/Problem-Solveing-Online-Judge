from typing import List 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        return nums
    
s = Solution()
print(s.sortColors([0,1,2,2,1,0,0]))