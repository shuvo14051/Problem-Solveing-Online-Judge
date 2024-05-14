from typing import *

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        first = 0
        second = 1
        li2 = [pref[0]]
        while second<len(pref):
            li2.append(pref[first]^pref[second])
            first += 1
            second += 1
        
        return li2