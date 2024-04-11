from typing import List 

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        length = len(startTime)
        count = 0
        for i in range(length):
            if queryTime >= startTime[i] and endTime[i] >= queryTime:
                count += 1

        return count
    

s = Solution()
print(s.busyStudent(startTime = [4], endTime = [4], queryTime = 4))