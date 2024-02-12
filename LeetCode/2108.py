from typing import List 

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            res = ""
            if i == i[::-1]:
                res = i
                break
        return res
    

