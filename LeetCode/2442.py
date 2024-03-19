from typing import List 

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums_copy = nums[:]
        for num in nums:
            nums_copy.append(int(str(num)[::-1]))
        
        s = set(nums_copy)
        return len(s) 
    
s = Solution()
print(s.countDistinctIntegers([1,13,10,12,31]))