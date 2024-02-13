from typing import List 
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        values = counter.values()
        set_values = set(values)
        if len(set_values) == len(values):
            return True
        return False