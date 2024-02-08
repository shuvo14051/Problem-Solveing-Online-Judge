class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        minimum_length = min(len(word1), len(word2))
        for i in range(minimum_length):
            result += word1[i] + word2[i]
        if len(word1) > minimum_length:
            result = result + word1[minimum_length:]
        if len(word2) > minimum_length:
            result = result + word2[minimum_length:]

        return result
    
s = Solution()
print(s.mergeAlternately("ab", "pqrs"))
        