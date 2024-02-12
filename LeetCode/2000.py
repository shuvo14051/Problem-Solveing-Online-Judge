class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        index_ch = word.index(ch)
        reverse_str = word[:index_ch+1][::-1] + word[index_ch+1:]
        return reverse_str
    

s = Solution()
print(s.reversePrefix("xyxzxe", "z"))