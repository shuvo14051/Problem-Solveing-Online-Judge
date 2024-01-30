# from collections import Counter

# def repeatedString(s, n):
#     count_per_repetition = Counter(s)

#     multiply = n // len(s)
    
#     rest = n - (len(s) * multiply)
    
#     # just count the "a" don't need to bother about other characters
#     count = count_per_repetition['a'] * multiply + Counter(s[:rest])['a']

#     return count

# result = repeatedString("a", 1000000000000)
# print(result)

from collections import Counter

def repeatedString(s, n):
    count_per_repetition = Counter(s)

    multiply = n // len(s)
    
    rest = n - (len(s) * multiply)
    
    count = count_per_repetition['a'] * multiply + Counter(s[:rest])['a']

    return count

result = repeatedString("a", 1000000000000)
print(result)
