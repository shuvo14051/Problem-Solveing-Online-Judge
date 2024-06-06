from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings_set = set()
        for meeting in meetings:
            meetings_set.update(range(meeting[0], meeting[1] + 1))
        
        count = 0
        for day in range(1, days + 1):
            if day not in meetings_set:
                count += 1
        
        return count
    
s = Solution()
print(s.countDays(days = 5, meetings = [[2,4],[1,3]]))