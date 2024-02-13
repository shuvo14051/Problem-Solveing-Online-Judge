from itertools import combinations

class Solution:
    def countVowelStrings(self, n: int) -> int:
        base = ["a","e","i","o","u"]
        pairs = combinations(base, n)

        return len(list(pairs))
    
s = Solution()
print(s.countVowelStrings(33))