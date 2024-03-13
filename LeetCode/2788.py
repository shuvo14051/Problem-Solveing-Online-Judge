from typing import List 

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        output = []
        final_output = []
        for i in words:
            output.extend(i.split(separator))
        for i in output:
            if i:
                final_output.append(i)
        return final_output
    
s = Solution()
print(s.splitWordsBySeparator(words = ["|||"], separator = "|"))