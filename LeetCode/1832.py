class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        li = [i.lower() for i in sentence]
        s = set(li)
        if len(s) == 26:
            return True
        return False
    
s = Solution()
print(s.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
    