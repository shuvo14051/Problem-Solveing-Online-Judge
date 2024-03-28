from collections import Counter

class Solution:
    def beautySum(self, s: str) -> int:
        length = len(s)
        sub = []
        result = 0
        for start in range(length):
            for end in range(start+1, length+1):
                sub.append(s[start:end])
        
        for ar in sub:
            counter = Counter(ar)
            vals = list(counter.values())
            result += max(vals) - min(vals)

        return result
    
s = Solution()
print(s.beautySum("aabcb"))