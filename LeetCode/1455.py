class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        
        for index, word in enumerate(words, 1):
            if word.startswith(searchWord):
                return index
        
        return -1
    
s = Solution()
print(s.isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg"))