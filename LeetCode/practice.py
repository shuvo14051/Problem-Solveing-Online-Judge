s = "abciiidef"
n = 3
li = []
li_v = []
def count_vowel(string):
    count = 0
    for i in string:
        if i in "aeiou":
            count += 1
    return count
for i in range(len(s)):
    li.append(s[i:3+i])
for i in li:
    li_v.append(count_vowel(i))
