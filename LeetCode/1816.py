class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        li = s.split(" ")
        result = " ".join(li[:k])
        return result
    
s = Solution()
print(s.truncateSentence("Hello how are you Contestant", 4))