from typing import List 

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = []
        for i in words:
            for j in words:
                if j == i:
                    continue
                elif j in i and j not in output:
                    output.append(j)

        return output
    
s = Solution()
print(s.stringMatching(words = ["leetcoder","leetcode","od","hamlet","am"]))