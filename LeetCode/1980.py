from typing import List 

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        li = [format(i, 'b').zfill(n) for i in range(2**n)]

        for i in li:
            if i not in nums:
                return i
    
s = Solution()
print(s.findDifferentBinaryString(["01","10"]))