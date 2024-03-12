from typing import List 

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        s = 0
        c = 0
        for i in costs:
            if s+i > coins:
                break
            else:
                s += i
                c += 1
        return c
    
s = Solution()
print(s.maxIceCream(costs = [1,3,2,4,1], coins = 7))