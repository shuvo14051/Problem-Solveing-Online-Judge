class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split(" ")
        new_li = []
        for i in li:
            new_li.append(i[::-1])
        string = " ".join(i for i in new_li)
        return string
    

s = Solution()
print(s.reverseWords("shuvo ji the boss"))