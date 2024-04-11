from typing import List 

"""
[1,1] --> 2
[2,3] --> 4
[0,9] --> 9
[0,2,0] --> 2
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        elif len(heights) == 2:
            if heights[0] == 0 or heights[1] == 0:
                return max(heights[0], heights[1])
            else:
                return min(heights)*2
            
        li = []

        for i in range(1, len(heights)-1):
            if min(heights[i-1], heights[i]) == 0:
                ma = max(heights[i-1], heights[i])
                ma2 = max(heights[i], heights[i+1])
                li.append(ma)
                li.append(ma2)
            m = min(heights[i-1], heights[i])
            m2 = min(heights[i-1], heights[i])
            li.append(m)
            li.append(m2)


        return max(li) * 2


s = Solution()
print(s.largestRectangleArea([1,1]))
print(s.largestRectangleArea([2,3]))
print(s.largestRectangleArea([0,9]))
print(s.largestRectangleArea([2,1,5,6,2,3]))