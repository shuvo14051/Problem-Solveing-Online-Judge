class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = s.count(letter)
        length = len(s)
        percentage = int((count / length ) * 100)

        return percentage

s = Solution()
print(s.percentageLetter(s = "foobar", letter = "o"))