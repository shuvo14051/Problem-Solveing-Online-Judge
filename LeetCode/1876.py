
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        window = 3
        count = 0
        for i in range(len(s)-window+1):
            set_i = set(s[i:i+window])
            if len(set_i) == 3:
                count += 1
        return count

s =  Solution()
print(s.countGoodSubstrings("xyzzaz"))