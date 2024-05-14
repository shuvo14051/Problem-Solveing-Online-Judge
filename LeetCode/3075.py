from typing import List 

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = sorted(happiness, reverse=True)
        result = 0
        for i in range(k):
            result += max(0, happiness[i] - i)

        return result

# class Solution:
#     def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
#         happiness = sorted(happiness, reverse=True)
#         result = 0
#         for i in range(k):
#             result += happiness[0]
#             happiness.remove(happiness[0])
#             happiness = [i-1 if i>0 else i for i in happiness]

#         return result
    
# s = Solution()
# print(s.maximumHappinessSum(happiness = [1,2,3], k = 2))

