from typing import List 

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        li = []
        for num in range(left, right+1):
            if "0" in str(num):
                continue
            self_dividing = True
            for i in str(num):
                if num % int(i) != 0:
                    self_dividing = False
                    break
            if self_dividing:
                li.append(num)
        return li
    
s = Solution()
print(s.selfDividingNumbers(47, 85))