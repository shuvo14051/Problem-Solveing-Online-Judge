from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()  
        max_sum = 0
        total_sum = 0
        for i in range(len(satisfaction) - 1, -1, -1):
            total_sum += satisfaction[i]
            if total_sum <= 0:
                break
            max_sum += total_sum
        return max_sum

s = Solution()
print(s.maxSatisfaction([-1,-8,0,5,-9])) 
