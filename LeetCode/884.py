from typing import List 

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        output = []
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        for i in s1:
            if i not in s2 and i not in output and s1.count(i) == 1:
                output.append(i)
        for j in s2:
            if j not in s1 and j not in output and s2.count(j) == 1:
                output.append(j)

        return output
    
s = Solution()
print(s.uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))