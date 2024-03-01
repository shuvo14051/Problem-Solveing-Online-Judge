from typing import List 

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        li = []
        for i in strs:
            if i.isdigit():
                 li.append(int(i))
            else:
                li.append(len(i))

        return max(li)

s = Solution()
print(s.maximumValue(["alic3","bob","3","4","00000"]))