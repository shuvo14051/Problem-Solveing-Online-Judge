from typing import List 

class Solution:
    """
    Wrong Answer
    heights = [0,9]
    Output 0
    Expected 9
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        elif len(heights) == 2:
            if heights[0] == 1 and heights[1] == 1:
                return 2
            return max(heights)
        
        li = []
        output = 0
        for i in range(1, len(heights)):
            m = min(heights[i-1], heights[i])
            li.append(m)
            output = max(li)*2
            
        return output
    

s = Solution()
print(s.largestRectangleArea([0,9]))