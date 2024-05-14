from typing import List 

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        diag1 = sum([mat[i][i] for i in range(n)])
        diag2 = sum([mat[i][n-1-i] for i in range(n)])
        common_element = mat[n//2][n//2] if n%2 == 1 else 0

        return  diag1 + diag2 - common_element
    


s = Solution()
print(s.diagonalSum(mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]))