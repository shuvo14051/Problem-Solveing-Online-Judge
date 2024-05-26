# from typing import List 
# import random

# class Solution:

#     def __init__(self, nums: List[int]):
#         self.li = nums
        

#     def pick(self, target: int) -> int:
#         if self.li.count(target) == 1:
#             return self.li.index(target)
#         else:
#             for num in self.li:
#                 indices = [i for i, val in enumerate(self.li) if val == num]
        
#         return random.choice(indices)
    

s = Solution([1, 2, 3, 3, 3])
print(s.pick(3))




# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)