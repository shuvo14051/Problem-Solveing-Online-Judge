from typing import List 
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        possible_outputs = []
        for key, value in counter.items():
            if key == value:
                possible_outputs.append(value)
        if possible_outputs:
            return max(possible_outputs)
        return -1
    
s = Solution()
print(s.findLucky([2,2,3,4]))