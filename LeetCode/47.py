from typing import List 
import itertools

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        li = set(list(itertools.permutations(nums)))
        result = []
        for item in li:
            result.append(list(item))
        return result
    
s = Solution()
print(s.permuteUnique(nums = [1,2,3]))