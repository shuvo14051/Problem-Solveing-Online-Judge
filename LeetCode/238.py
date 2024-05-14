from typing import List 


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        return [l*r for l, r in zip(prefix, suffix)]
    
s = Solution()
print(s.productExceptSelf(nums = [1,2,3,4]))
