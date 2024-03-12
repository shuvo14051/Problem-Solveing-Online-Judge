from math import comb
from typing import List 
from itertools import combinations

class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n + 1), k))
    
s = Solution()
print(s.combine(4,2))