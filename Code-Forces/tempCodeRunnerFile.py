test = int(input())

for _ in range(test):
    count = 0
    n = int(input())
    for i in range(1, n+1):
        # Count the number of unique digits in i
        unique_digits = len(set(str(i)))
        if unique_digits == 1:
            count += 1
    print(count)
