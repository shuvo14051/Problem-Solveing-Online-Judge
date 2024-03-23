from typing import List 

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        d = {}
        li = []
        for i in range(len(mat)):
            d[i] = mat[i].count(1)

        max_value = max(list(d.values()))
        for key, val in d.items():
            if val == max_value:
                li.append(key)
                li.append(val)
            if li:
                break
        return li
    
s = Solution()
print(s.rowAndMaximumOnes([[0,0],[1,1],[0,0]]))
