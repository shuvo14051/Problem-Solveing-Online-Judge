from typing import List 

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        li = s.split(":")
        result_li = []

        start_ch = li[0][0]
        start_num = int(li[0][1])

        end_ch = li[1][0]
        end_num = int(li[1][1])

        start_ascii = ord(start_ch)
        end_ascii = ord(end_ch)

        for i in range(start_ascii, end_ascii+1):
            for j in range(start_num, end_num+1):
                result_li.append(chr(i) + str(j))
        
        
        return result_li
    

s = Solution()
print(s.cellsInRange("K1:L2"))