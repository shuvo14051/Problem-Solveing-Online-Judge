class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        li = sentence.split(' ')
        first, nextt = 0, 1
        if len(li) <= 1:
                return True
        while nextt < len(li):
            if li[first][-1] != li[nextt][0]:
                return False
            first += 1
            nextt += 1
        return True
    
s = Solution()
print(s.isCircularSentence("Leetcod"))
        