class Solution:
    def repeatedCharacter(self, s: str) -> str:
        set_of_word = set()
        for char in s:
            if char in set_of_word:
                return char
            else:
                set_of_word.add(char)
            
s = Solution()
print(s.repeatedCharacter("acdavdr"))