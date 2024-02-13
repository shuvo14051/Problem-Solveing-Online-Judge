from typing import List 

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        li = []
        for i in details:
            age = int(i[-4:-2])
            if age > 60:
                count += 1
        return count
        

s = Solution()
print(s.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))