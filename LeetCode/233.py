# Time limit exceeded

class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            s = str(i)
            one = s.count("1")
            count += one
        return count