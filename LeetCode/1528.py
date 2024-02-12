from typing import List 

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {}
        string = ""
        for i in range(len(s)):
            d[indices[i]] = s[i]

        d = dict(sorted(d.items()))
        for key, val in d.items():
            string += val

        return string

    


s = Solution()
print(s.restoreString("codeleet", [4,5,6,7,0,2,1,3]))