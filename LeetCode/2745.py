class Solution:
    def sortVowels(self, s: str) -> str:
        li = list(s)
        vowel_index = []
        vowels = ""
        for index, value in enumerate(s):
            if value in "aeiouAEIOU":
                vowel_index.append(index)
                vowels += value
        sorted_vowels = "".join(sorted(vowels))

        for i in range(len(sorted_vowels)):
            li[vowel_index[i]] = sorted_vowels[i]

        result = "".join(li)
        return result

s = Solution()
print(s.sortVowels("shuvOji"))