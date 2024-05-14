from typing import List 

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if (m*n) != len(original):
            return []
        
        two_d_array = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                two_d_array[i][j] = original[i * n + j]
        
        return two_d_array

    
s = Solution()
print(s.construct2DArray(original = [1,2,4], m = 1, n = 3))
