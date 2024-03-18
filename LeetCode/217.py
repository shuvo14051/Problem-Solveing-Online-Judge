from typing import List 
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        result = False
        for key, value in c.items():
            if value >= 2:
                result = True
                break
        return result