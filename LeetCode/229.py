from typing import List 
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        result = []
        length = len(nums)
        condition = length // 3
        for key, val in counter.items():
            if val > condition:
                result.append(key)

        return result

s = Solution()
print(s.majorityElement(nums = [1,2]))
