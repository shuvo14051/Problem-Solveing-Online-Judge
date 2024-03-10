# from typing import List 

# class Solution:
#     def evenOddBit(self, n: int) -> List[int]:
#         even, odd = 0, 0
#         binary = bin(n)[2:]
#         for index, value in enumerate(binary):
#             if value == "1":
#                 if index % 2 == 0:
#                     even += 1
#                 else:
#                     odd += 1
#         return [even, odd]
    
# s = Solution()
# print(s.evenOddBit(17))
