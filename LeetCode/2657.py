from typing import List 

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = []
        for i in range(len(A)):
            set1 = set(A[:i+1])
            set2 = set(B[:i+1])
            result.append(len(set1.intersection(set2)))

        return result
    
s = Solution()
print(s.findThePrefixCommonArray(A = [2,3,1], B = [3,1,2]))