from typing import List 
from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s = 0
        counter = Counter(nums)
        for key, value in counter.items():
            if value == 1:
                s += key

        return s

