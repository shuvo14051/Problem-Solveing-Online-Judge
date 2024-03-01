class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while True:
            if n <= 1:
                break
            if n%2 == 0:
                n = n // 2
                matches += n 
            elif n%2 == 1:
                n = n // 2 + 1
                matches += n
        return matches
s = Solution()
print(s.numberOfMatches(14))