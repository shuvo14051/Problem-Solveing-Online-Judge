from typing import List 

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        d = {}
        result = []
        for ar in score:
            d[ar[k]] = ar
        d = dict(sorted(d.items(), key = lambda x: x[0], reverse=True))
        for val in d.values():
            result.append(val)

        return result
    
s =  Solution()
print(s.sortTheStudents(score = [[3,4],[5,6]], k = 0))