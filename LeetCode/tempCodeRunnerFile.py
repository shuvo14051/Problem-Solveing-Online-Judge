class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        li = s.split()
        li2 = sorted(li, reverse=False)
        return " ".join(x for x in li2)