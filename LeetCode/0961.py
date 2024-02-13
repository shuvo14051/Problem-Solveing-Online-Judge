from typing import List 
from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        counter = Counter(nums)
        for key, value in counter.items():
            if value == n:
                return key