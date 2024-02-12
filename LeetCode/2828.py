from typing import List 

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        s2 = ""
        for i in words:
            s2 += i[0]

        return s == s2