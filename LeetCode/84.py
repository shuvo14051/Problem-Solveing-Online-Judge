# from typing import List 

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         if len(heights) == 1:
#             return heights[0]
#         li = []
#         output = 0
#         for i in range(1, len(heights)):
#             m = min(heights[i-1], heights[i])
#             li.append(m)
#             output = max(li)*2
            
#         return output

# s = Solution()
# print(s.largestRectangleArea([2]))