from typing import List 

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sums = []
        for row in mat:
            sums.append(sum(row))

        d = {}
        for index, value in enumerate(sums):
            d[index] = value
        
        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
        keys = list(sorted_dict.keys())[:k]
        return keys
    

s = Solution()
print(s.kWeakestRows(
    [[1,1,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,1,1]], 3))