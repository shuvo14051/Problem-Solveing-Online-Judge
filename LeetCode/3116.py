# from typing import List 

# class Solution:
#     def findKthSmallest(self, coins: List[int], k: int) -> int:
#         multiples = []
#         for num in coins:
#             multiples.extend([num * i for i in range(1, k + 1)])

#         unique_sorted_multiples = sorted(set(multiples))
#         result = unique_sorted_multiples[k-1]
        
#         return result
    
# s = Solution()
# print(s.findKthSmallest(coins = [3,6,9], k = 3))