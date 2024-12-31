from typing import List 
from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result = []
        counter = Counter(nums)
        for key, val in counter.items():
            if val == 2:
                result.append(key)

        return result
    
s = Solution()
print(s.getSneakyNumbers([0,0,1,1,2]))