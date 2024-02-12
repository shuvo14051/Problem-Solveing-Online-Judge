from typing import List
from collections import Counter

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        sorted_li = []
        pairs = 0
        for i in words:
            string = "".join(sorted(i))
            sorted_li.append(string)
        counter = Counter(sorted_li)
        for value in counter.values():
            if value>1:
                pairs += 1

        return pairs
    
s = Solution()
print(s.maximumNumberOfStringPairs(["aa","ab"]))


