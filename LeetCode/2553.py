from typing import List 

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        li = []
        for i in nums:
            li.extend(list(str(i)))
        li = [int(i) for i in li]

        return li
    
s = Solution()
print(s.separateDigits([13,25,83,77]))