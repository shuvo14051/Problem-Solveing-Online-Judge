
# Time limit exceeded
"""
import heapq 

class MedianFinder:

    def __init__(self):
        self.values = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.values, num)

    def findMedian(self) -> float:
        values_sorted = sorted(self.values)
        n = len(values_sorted)
        if n % 2 == 0:
            mid_left = n // 2 - 1
            mid_right = n // 2
            median = (values_sorted[mid_left] + values_sorted[mid_right]) / 2
        else:
            median = values_sorted[n // 2]
        
        return median
        
"""

