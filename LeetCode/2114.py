from typing import List 

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = []
        for sentence in sentences:
            sentence_li = sentence.split(" ")
            result.append(len(sentence_li))

        return max(result)