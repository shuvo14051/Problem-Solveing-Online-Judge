from typing import List 

class Solution:
    def countBits(self, n: int) -> List[int]:
        li = []
        for i in range(n+1):
            binary = bin(i)[2:]
            li.append(binary.count("1"))    

        return li