from typing import List 

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        li = [str(i) for i in range(1,n+1)]
        sorted_li = sorted(li)
        int_li = [int(i) for i in sorted_li]
        return int_li
    
s = Solution()
print(s.lexicalOrder(13))