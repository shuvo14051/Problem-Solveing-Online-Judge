from collections import Counter

numbers = [1, 2, 3, 4, 1, 2, 3, 1, 1]
counter = Counter(numbers)

# Iterate over the counter and print counts of elements with duplicates
for num, count in counter.items():
    if count > 1:
        print(f"{num} has {count} duplicates.")
