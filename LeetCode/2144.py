from typing import List 

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        s = 0
        for i in range(len(cost)):
            if i!=0 and (i+1) % 3 == 0:
                pass
            else:
                s+=cost[i]
        return s
    
s = Solution()
print(s.minimumCost([10,5,9,4,1,9,10,2,10,8]))
