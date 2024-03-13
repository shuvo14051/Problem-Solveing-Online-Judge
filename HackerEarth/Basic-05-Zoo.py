from collections import Counter

word = input()
counter = Counter(word)
values = list(counter.values())
if values[-1] == values[0]:
    print("No")
elif values[-1] % values[0] == 0:
    print("Yes")
else:
    print("No")