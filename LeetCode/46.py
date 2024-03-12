from typing import List 
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        perm = list(permutations(nums))
        for i in perm:
            output.append((list(i)))
        return output
    
s = Solution()
print(s.permute([1,3,2]))