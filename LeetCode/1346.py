from typing import List 

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in arr:
            if i*2 in arr:
                return True

        return False
        
s = Solution()
print(s.checkIfExist([-2,0,10,-19,4,6,-8]))