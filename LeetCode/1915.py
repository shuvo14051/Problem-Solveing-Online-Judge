# from collections import Counter

# class Solution:
#     def check(self, word):
#         counter = Counter(word)
#         keys = list(counter.values())
#         count = 0 
#         for occurance in keys:
#             if occurance % 2 != 0:
#                 count += 1
#         if count <= 1:
#             return True
#         return False
    
#     def wonderfulSubstrings(self, word: str) -> int:
#         li = []
#         for i in range(len(word)):
#             for j in range(len(word)+1):
#                 if word[i:j]:
#                     li.append(word[i:j])

#         result = 0
#         for i in  li:
#             if self.check(i):
#                 result += 1
#         return result
    
s = Solution()
print(s.wonderfulSubstrings("aba"))