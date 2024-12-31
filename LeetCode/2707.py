from typing import List 

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        s2 = "".join(dictionary)
        count = 0
        for i in s:
            if i not in s2:
                count += 1

        return count
    
s = Solution()
print(s.minExtraChar(s = "sayhelloworld", dictionary = ["hello","world"]))