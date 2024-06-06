# from typing import List 

# class Solution:
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#         if len(hand) % groupSize != 0:
#             return False
#         else:
#             while hand:
#                 m = min(hand)
#                 for i in range(groupSize):
