# class Solution:
#     def passThePillow(self, n: int, time: int) -> int:
#         li = list(range(1, n+1))
#         print(li)
#         if n > time:
#             return li[time]
#         else:
#             extra = time - n + 1
#             n1 = extra // n
#             time1 = extra % n
#             print(extra, n1, time1)

#             if n1:
#                 li = li * n1
#             li = li + li[:time1] 

#             return li[time], li
    

# s = Solution()
# print(s.passThePillow(8,9))