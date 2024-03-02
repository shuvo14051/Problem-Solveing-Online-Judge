n, minutes = map(int, input().split())
count = 0
four_hours = 60 * 4

minutes_remaining = four_hours - minutes
summ = 0

for i in range(5, minutes_remaining+1, 5):
    summ += i
    if summ <= minutes_remaining:
        count += 1 

    if count == n:
        break

print(count)
