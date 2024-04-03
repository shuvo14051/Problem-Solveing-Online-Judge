class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        all_caps = all(i.isupper() for i in word)

        if all_caps:
            return True
        elif word[0].isupper() and all(j.islower() for j in word[1:]):
            return True
        elif all(j.islower() for j in word):
            return True
        return False
    

s = Solution()
print(s.detectCapitalUse("g"))