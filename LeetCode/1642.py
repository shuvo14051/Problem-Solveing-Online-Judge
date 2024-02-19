from typing import List 

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        count = 0
        for i in range(1, len(heights)):
            if heights[i-1] >= heights[i]:
                count += 1
            elif heights[i-1] < heights[i] and bricks:
                bricks = bricks - (heights[i] - heights[i-1])
                count += 1
                continue
            elif heights[i-1] < heights[i] and bricks:
                ladders = ladders - 1
                count += 1

        return count
    

s = Solution()
print(s.furthestBuilding(heights = [14,3,19,3], bricks = 17, ladders = 0))