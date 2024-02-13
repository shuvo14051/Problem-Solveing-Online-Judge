from typing import List 

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in nums:
            if i%2 == 0:
                even.append(i)
            elif i%2 == 1:
                odd.append(i)
        
        return even + odd
    

s = Solution()
print(s.sortArrayByParity([3,2,4,1]))