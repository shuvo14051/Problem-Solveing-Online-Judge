from collections import Counter

while True:
    a, b = map(int, input().split())
    string = ""
    if a == 0 and b == 0:
        break
    for i in range(a, b+1):
        string += str(i)
    char_count = Counter(string)
    if len(char_count) == 9:
        pass
    print(list(char_count.values()))

