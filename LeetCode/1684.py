from typing import List 

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count =  0
        for i in words:
            item = list(i)
            s = set(item)
            li = list(s)
            consistent = True
            new_string = "".join(li)
            for j in new_string:
                if j not in allowed:
                    consistent = False
                    break
            if consistent:  
                count += 1

        return count


s = Solution()
print(s.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"])) 