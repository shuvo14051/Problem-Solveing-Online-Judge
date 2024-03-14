from typing import List 

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        output = set(nums[0])
        for i in range(1, len(nums)):
            output = output.intersection(nums[i])
        output = sorted(list(output))
        return (output)
    
s = Solution()
print(s.intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))