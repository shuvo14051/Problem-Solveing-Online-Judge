from typing import List 
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        answer = 0
        maximum = max(counter.values())
        for value in counter.values():
            if value == maximum:
                answer += value

        return answer