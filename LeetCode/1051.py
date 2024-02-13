from typing import List 

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_height = sorted(heights)
        count = 0
        for i in range(len(new_height)):
            if heights[i] != new_height[i]:
                count += 1

        return count