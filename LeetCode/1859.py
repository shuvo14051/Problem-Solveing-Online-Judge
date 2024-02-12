class Solution:
    def sortSentence(self, s: str) -> str:
        li = s.split(' ')
        print(li)
        num_first = [i[-1] + i[0:len(i)-1] for i in li]
        sorted_li =  sorted(num_first)
        num_removed = [i[1:len(i)] for i in sorted_li]
        string = " ".join(i for i in num_removed)
        return string
    
s = Solution()
print(s.sortSentence("Myself2 Me1 I4 and3"))