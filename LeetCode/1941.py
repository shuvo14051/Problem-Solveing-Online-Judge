from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter =  Counter(s)
        values = counter.values()
        unique_values = set(values)
        if len(unique_values) == 1:
            return True
        return False
    

s = Solution()
print(s.areOccurrencesEqual("abcabc")) 