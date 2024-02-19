from typing import List 
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        keys = counter.keys()
        values = counter.values()
        k_2 = 0
        for key, value in counter.items():
            if value >= 
                
s = Solution()
print(s.findLeastNumOfUniqueInts(arr = [4,3,1,1,3,3,2], k = 3))