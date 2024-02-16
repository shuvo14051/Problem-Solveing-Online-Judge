from typing import List 

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        n_2 = n*n
        missing = list(range(1,n_2+1))
        li = []
        res = []
        for i in grid:
            li.extend(i)
        
        for i in li:
            if li.count(i) == 2:
                res.append(i)
                break
        for i in missing:
            if i not in li:
                res.append(i)
        return res
    
s = Solution()
print(s.findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))

