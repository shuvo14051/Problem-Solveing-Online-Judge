from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result_li = []
        for idx, word in enumerate(words):
            if x in word:
                result_li.append(idx)

        return result_li
    
s = Solution()
print(s.findWordsContaining(["aaa","aaa","aaa","aaa"], "a"))