from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        output = ""
        counter = Counter(s)
        sorted_counter = dict(sorted(counter.items(), key=lambda item: -item[1]))
        for key, value in sorted_counter.items():
            output += key*value
        return output
    

s = Solution()
print(s.frequencySort("abcc"))