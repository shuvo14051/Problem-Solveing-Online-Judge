# class Solution:
#     def nearestPalindromic(self, n: str) -> str:
#         palinrome = []
#         n1 = int(n)
#         n2 = int(n)
#         while True:
#             n1 = n1 - 1
#             if str(n1) == str(n1)[::-1]:
#                 palinrome.append(n1)
            
            
#             n2 = n2 + 1
#             if str(n2) == str(n2)[::-1]:
#                 palinrome.append(n2)
            

#             if len(palinrome) >= 2:
#                 break

#         return str(min(palinrome))
    
s = Solution()
print(s.nearestPalindromic(9))