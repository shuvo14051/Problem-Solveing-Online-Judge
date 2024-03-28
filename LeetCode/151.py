class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        print("Stripped: " ,s)
        li = s.split()
        print(li)
        li2 = li[::-1]
        print(li2)
        return " ".join(x for x in li2)
    
s = Solution()
print(s.reverseWords("  hello world  "))