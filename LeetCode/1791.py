from typing import List 
from collections import Counter

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        li = []
        for i in edges:
            li.extend(i)
        counter = Counter(li)
        root = max(counter.values())
        for key, value in counter.items():
            if value == root: 
                return key
    

s = Solution()
print(s.findCenter([[1,2],[2,3],[4,2]]))
