from typing import List 

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0
        for i in words1:
            if i in words2 and words1.count(i) == 1 and words2.count(i) == 1:
                count += 1
        return count
        
