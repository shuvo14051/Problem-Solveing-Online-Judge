from typing import List  

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peak = []
        for i in range(1, len(mountain)-1):
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                peak.append(i)

        return peak 
    

s = Solution()
print(s.findPeaks([1,4,3,8,5]))

