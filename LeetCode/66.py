from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''.join(map(str, digits))
        integer = int(string)
        integer += 1
        string = str(integer)
        li = [int(i) for i in string]

        return li
    
s = Solution()
print(s.plusOne([9]))
        