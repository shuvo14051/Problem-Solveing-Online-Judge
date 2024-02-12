class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        length = len(s) // 2
        first = s[:length]
        second = s[length:]
        first_vowel = 0
        secnd_vowel = 0

        for i in range(length):
            if first[i] in 'aeiou':
                first_vowel += 1
            if second[i] in 'aeiou':
                secnd_vowel += 1

        if first_vowel == secnd_vowel:
            return True
        
        return False
    

s = Solution()
print(s.halvesAreAlike("textbook"))
