n, minutes = map(int, input().split())
count = 0
four_hours = 60 * 4

# minutes_remaining for solving problem
minutes_remaining = four_hours - minutes
summ = 0

for i in range(5, minutes_remaining, 5):
    summ += i
    print(summ)  # Corrected the variable name from sum to summ
    if count == n:
        break
    count += 1  # Moved the count increment outside the if condition

print(count)
