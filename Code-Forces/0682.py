from typing import List 

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        li = []
        for i in operations:
            if (i.isdigit()) or (i[0] == '-' and i[1:].isdigit()):
                li.append(int(i))
            elif i == "C":
                li.pop()
            elif i == "D":
                li.append(li[-1]*2)
            elif i == "+":
                li.append(li[-2]+li[-1])
        return sum(li)
    
s = Solution()
print(s.calPoints(["5","-2","4","C","D","9","+","+"]))