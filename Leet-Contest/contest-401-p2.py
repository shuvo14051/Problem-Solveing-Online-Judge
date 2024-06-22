# class Solution:
#     def valueAfterKSeconds(self, n: int, k: int) -> int:
#         li = [1]*n

#         for _ in range(len(li) - 1):
#             new_arr = []
#             for i in range(len(li)):
#                 new_arr.append(sum(li[:i+1]))
#             li = new_arr
#         return li
    
# s = Solution()
# print(s.valueAfterKSeconds(4,5))