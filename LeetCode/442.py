from typing import List 
from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        counter = Counter(nums)
        for key, value in counter.items():
            if value == 2:
                output.append(key)
        return output
    

        
