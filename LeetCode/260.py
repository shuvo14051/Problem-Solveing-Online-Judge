from typing import List 

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = []
        counter = Counter(nums)
        for key, val in counter.items():
            if val == 1:
                result.append(key)

        return result
