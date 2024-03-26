from typing import List 
from math import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        c = []
        output = []
        for point in points:
            result = sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            c.append((point, result))

        sorted_c = sorted(c, key=lambda x: x[1])
        for i in sorted_c[:k]:
            output.append(i[0])

        return output

s = Solution()
print(s.kClosest([[1,3],[-2,2]], 1))