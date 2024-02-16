# class Solution:
#     def repeatedCharacter(self, s: str) -> str:
#         for i in range(1, len(s)):
#             if s[i-1] == s[i]:
#                 return s[i]
#             if s.count(s[i]) == 2:
#                 return s[i]
            
# s = Solution()
# print(s.repeatedCharacter("hthg"))