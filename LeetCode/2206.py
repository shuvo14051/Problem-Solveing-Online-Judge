from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        count = 0
        for val in counter.values():
            
            if val % 2 !=0 :
                return False
        return True
    
