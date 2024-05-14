class Solution:
    def arrangeWords(self, text: str) -> str:
        text_li = text.split(" ")
        sorted_text = sorted(text_li, key=len)
        result = " ".join(sorted_text).capitalize()
        return result
    
s = Solution()
print(s.arrangeWords("Leetcode is cool"))