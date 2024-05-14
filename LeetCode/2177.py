from typing import List 

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3 == 0:
            num = num // 3
            return [num-1, num, num+1]
        return [] 

s = Solution()
print(s.sumOfThree(4))

# Time limit
# class Solution:
#     def sumOfThree(self, num: int) -> List[int]:
#         mid_val = num // 2
#         li = []
#         for i in range(1, mid_val+1):
#             if (i + (i + 1) + (i + 2)) == num:
#                 li = [i, i+1, i+2]
#                 break
        
#         return li
    




