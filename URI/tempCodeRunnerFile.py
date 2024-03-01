from collections import Counter

while True:
    try:
        stirng = input().strip()
        counter = Counter(stirng)
        sorted_items = sorted(counter.items(), key=lambda item: (-item[1], ord(item[0])))
        for key, value in sorted_items.items():
            print(ord(key), value)
        print()

    except EOFError:
        break