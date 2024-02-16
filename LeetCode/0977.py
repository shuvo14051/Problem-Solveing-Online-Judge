from typing import List 

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [i**2 for i in nums]

        squares.sort()

        return squares
    
s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))