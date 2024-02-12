from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        li = []
        res_li = []
        for i in image:
            li.append(i[::-1])
        for i in li:
            for j in i:
                single_operation = [j-1 if j==1 else j+1 for j in i]
            res_li.append(single_operation)

        return res_li
    
s = Solution()
print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))