from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = 0
        n = len(hours)
        
        for l in range(n):
            for r in range(l + 1, n):
                if (hours[l] + hours[r]) % 24 == 0:
                    count += 1
        
        return count
    
s = Solution()
print(s.countCompleteDayPairs(hours = [72, 48, 24, 3]))  # Expecting 3
