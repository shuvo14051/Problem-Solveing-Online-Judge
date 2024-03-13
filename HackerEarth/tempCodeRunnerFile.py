from collections import Counter

word = input()
counter = Counter(word)
keys = counter.keys()
if keys[-1] % keys[0] == 0:
    print("Yes")
else:
    print("No")