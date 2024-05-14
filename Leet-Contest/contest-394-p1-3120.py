class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word.lower())
        count = 0
        for char in s:
            if char.upper() in word and char.lower() in word:
                count+=1
        return count
    

s = Solution()
print(s.numberOfSpecialChars("abBCab"))