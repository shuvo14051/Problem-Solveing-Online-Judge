class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 1:
            if n % 2 == 0:
                matches += n // 2
                n //= 2
            else:
                matches += n // 2
                n = n // 2 + 1
        return matches

s = Solution()
print(s.numberOfMatches(2))  # Output should be 13
