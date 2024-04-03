from typing import List
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
               "6":"mno","7":"pqrs","8":"tuv", "9":"wxyz"}
        if digits == "":
            return []
        
        var = [dic[digit] for digit in digits]
        result = list(product(*var))
        final = [''.join(comb) for comb in result]
        return final
    
s = Solution()
print(s.letterCombinations("233"))