class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        letters = "abcdefghij"
        d = {}
        first, second, target = "", "", ""

        for idx, word in enumerate(letters):
            d[word] = str(idx)

        for i in firstWord:
            if i in d.keys():
                first += d[i]
        for i in secondWord:
            if i in d.keys():
                second += d[i]
        for i in targetWord:
            if i in d.keys():
                target += d[i]

        if int(first) + int(second) == int(target):
            return True
        
        return False

s = Solution()
print(s.isSumEqual(firstWord = "acb", secondWord = "cba", targetWord = "cdb"))