# from typing import List 

# class Solution:
#     def replaceWords(self, dictionary: List[str], sentence: str) -> str:
#         li = sentence.split(' ')
#         output = ""
#         result = []
#         for index in range(len(li)):
#             for val in dictionary:
#                 if li[index].startswith(val):
#                     result.append(val)
#                     break
#             result.append(li[index])

#         output = " ".join(result)
#         return output
    
# s = Solution()
# print(s.replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"))