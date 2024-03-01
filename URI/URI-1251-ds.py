from collections import Counter

while True:
    try:
        stirng = input().strip()
        counter = Counter(stirng)
        sorted_items = sorted(counter.items(), key=lambda item: (item[1], ord(item[0])))
        for char, count in sorted_items:
            print(ord(char), count)

    except EOFError:
        break