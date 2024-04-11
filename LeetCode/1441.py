# from typing import List 

# class Solution:
#     def buildArray(self, target: List[int], n: int) -> List[str]:
#         result = []
#         for i in range(1,n+1):
#             if i in target:
#                 result.append("Push")
#             else:
#                 result.extend(["Push", "Pop"])

#         return result
    
# s = Solution()
# print(s.buildArray([1,2,3,4], 3))