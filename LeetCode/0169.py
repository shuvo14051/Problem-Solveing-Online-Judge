from typing import List 
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        m = max(counter.values())
        for key, value in counter.items():
            if value == m:
                return key
        
    
s = Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))