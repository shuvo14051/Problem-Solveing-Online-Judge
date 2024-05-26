from typing import List 
from itertools import chain, combinations
from functools import reduce
import operator



class Solution:

    def compute_xor(self, lst):
        if not lst:  # Handling empty list case
            return 0
        return reduce(operator.xor, lst)

    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        li = list(chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1)))

        li2 = []
        for i in li:
            li2.append(list(i))
            
        xor_results = [self.compute_xor(lst) for lst in li2]
    
        return sum(xor_results)
    

s = Solution()
print(s.subsetXORSum([5,1,6]))