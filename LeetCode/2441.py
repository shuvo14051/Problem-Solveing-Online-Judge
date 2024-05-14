from typing import List 

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            if i > 0 and i*-1 in nums:
                result = max(result, i)

        if result:
            return result
        return -1
s = Solution()
print(s.findMaxK([-1,10,6,7,-7,1]))
