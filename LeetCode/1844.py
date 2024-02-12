class Solution:
    def replaceDigits(self, s: str) -> str:
        for i in range(len(s)):
            if s[i].isdigit():
                val = s[i-1]
                ascii_val = ord(val)
                new_char_ascii = ascii_val + int(s[i])
                new_char = chr(new_char_ascii)
                s = s.replace(s[i], new_char, 1)

        return s
    

s = Solution()
print(s.replaceDigits('a1c1e1'))