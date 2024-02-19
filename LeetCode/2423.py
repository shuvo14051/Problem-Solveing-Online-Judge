from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        occurances = list(counter.values())
        s = set(occurances)
        if len(s) == 1:
            return True, occurances
        maximum = max(occurances)
        index_max = occurances.index(maximum)
        occurances[index_max] -= 1
        s = set(occurances)
        if len(s) == 1:
            return True, occurances
        return False, occurances

s = Solution()
print(s.equalFrequency("aazz"))
