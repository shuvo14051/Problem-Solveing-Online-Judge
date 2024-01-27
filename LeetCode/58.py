class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        li_s = s.split(" ")
        result = len(li_s[-1])

        return result
    

s = Solution()
print(s.lengthOfLastWord("luffy is still joyboy")) 