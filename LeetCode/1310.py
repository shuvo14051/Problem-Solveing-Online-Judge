from typing import List
from functools import reduce

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        for item in queries:
            xor_result = reduce(lambda x, y: x ^ y, arr[item[0]:item[1] + 1])
            result.append(xor_result)
        return result
    
s = Solution()
print(s.xorQueries(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]))
