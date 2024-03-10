from typing import List 

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n%2 == 0:
            li = []
        else:
            li = [0]
        for i in range(1,n//2+1):
            li.append(i)
            li.append(-i)

        return li 

s = Solution()
print(s.sumZero(5))