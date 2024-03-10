from typing import List 
from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        li = []
        for key, value in counter.items():
            if value == 1:
                li.append(key)
       
        if k > len(li):
            return ""
        else:
            return li[k-1]

s = Solution()
print(s.kthDistinct(arr = ["d","b","c","b","c","a"], k = 5))