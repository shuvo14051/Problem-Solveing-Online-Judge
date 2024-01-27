X, Y = map(int, input().split())
count = 0

for i in range(1, Y + 1):
    count += 1
    if count < X:
        print(i, end=' ')
    else:
        print(i)  # Print a newline when the count reaches X
        count = 0  # Reset the count

# Ensure there's no extra space after the last number
