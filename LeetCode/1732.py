from typing import List 

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        li = []
        s = 0
        for i in range(len(gain)):
            s = s + gain[i]
            li.append(s)

        m = max(li)
        if m < 0:
            return 0
        return m
    

s = Solution()
print(s.largestAltitude(gain = [-5,1,5,0,-7]))