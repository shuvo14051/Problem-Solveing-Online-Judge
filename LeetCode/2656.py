from typing import List 

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        s = 0
        nums.sort()
        for i in range(k):
            m = max(nums)
            s += nums.pop()
            nums.append(m+1)

        return s
    
s = Solution()
print(s.maximizeSum(nums = [5,5,5], k = 2))