# from typing import List 

# class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         sorted_people = sorted(people)
#         s = sorted_people[0]
#         count = 0
#         for i in range(1, len(people)):
#             if s < limit:
#                 s += sorted_people[i] 
#             elif s >= limit:
#                 count += 1

#         return count
    

# s = Solution()
# print(s.numRescueBoats(people = [1,2], limit = 3))