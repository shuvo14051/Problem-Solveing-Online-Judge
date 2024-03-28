class Solution:
    def palindrome(self, pattern):
            start = 0
            end = len(pattern)-1
            while start != end:
                if pattern[start] != pattern[end]:
                    return False
                return True
            
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_li = s.split(" ")
        if len(s_li) != len(pattern):
            return False
        check_pattern = self. palindrome(pattern)
        check_s = self.palindrome(s_li)

        return check_pattern and check_s

s = Solution()
print(s.wordPattern(pattern = "abba", s = "dog cat cat dog"))

    