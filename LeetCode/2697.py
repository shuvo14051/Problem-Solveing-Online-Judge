class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        start = 0
        end = len(s) - 1
        while start <= end:
            if s[start] != s[end]:
                if s[start] > s[end]:
                    s = s[:start] + s[end] + s[start + 1:]
                elif s[start] < s[end]:
                    s = s[:end] + s[start] + s[end + 1:]
            start += 1
            end -= 1

        return s

# Test cases
solution = Solution()
print(solution.makeSmallestPalindrome("bhh"))  # Output: "bhb"

