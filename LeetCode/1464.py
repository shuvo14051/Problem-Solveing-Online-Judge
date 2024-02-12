from typing import List
import itertools

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        li = []
        pairs =  itertools.combinations(nums, 2)
        for pair in pairs:
            li.append((pair[0]-1) * (pair[1]-1))

        return max(li)
    
s = Solution