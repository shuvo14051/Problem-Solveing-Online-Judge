from typing import List
from itertools import chain, combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return list(chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1)))
    
    