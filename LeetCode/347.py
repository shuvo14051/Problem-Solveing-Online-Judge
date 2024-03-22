from collections import Counter
from typing import List 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counter = Counter(nums)
        sorted_counter = sorted(counter.keys(), key=lambda x: -counter[x])

        return sorted_counter[:k]
    
s = Solution()
print(s.topKFrequent(nums =[4,1,-1,2,-1,2,3], k = 2))