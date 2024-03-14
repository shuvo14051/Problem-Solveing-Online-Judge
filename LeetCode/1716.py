# class Solution:
#     def totalMoney(self, n: int) -> int:
#         start = 1
#         temp_start = start
#         s = 0
#         count = 1
#         while count <= n:
#             s += temp_start
#             count += 1
#             temp_start = temp_start + 1
#             if count % 7 == 0:
#                 print("")
#                 start = start + 1
#                 temp_start = start 
#         return s
    
# s = Solution()
# print(s.totalMoney(10))