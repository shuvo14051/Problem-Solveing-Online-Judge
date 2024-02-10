class Solution:

    @staticmethod
    def count_vowel(string):
        count = 0
        for i in string:
            if i in "aeiou":
                count += 1
        return count
    
    def maxVowels(self, s: str, k: int) -> int:
        li = []
        li_v = []
        
        for i in range(len(s)):
            li.append(s[i:k+i])
        for i in li:
            li_v.append(self.count_vowel(i))

        return max(li_v)
    

s = Solution()
print(s.maxVowels("aeiou",2))