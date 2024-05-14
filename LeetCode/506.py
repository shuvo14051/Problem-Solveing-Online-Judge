from typing import List 

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = {}
        result = []
        
        for idx, value in enumerate(sorted(score, reverse=True)):
            if idx == 0:
                d[value] = ("Gold Medal")
            elif idx == 1:
                d[value] = ("Silver Medal")
            elif idx == 2:
                d[value] = ("Bronze Medal")
            else:
                d[value] = str(idx+1)

        for s in score:
            result.append(d[s])

        return result
    
s = Solution()
print(s.findRelativeRanks(score = [10,3,8,9,4]))

