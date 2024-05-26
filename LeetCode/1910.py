class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            print(s)
            s = s.replace(part, '', 1)

        return s
    
s = Solution()
print(s.removeOccurrences("daabcbaabcbc","abc"))