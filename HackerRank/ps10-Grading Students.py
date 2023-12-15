n = int(input())

for i in range(n):
    grade = int(input())
    next_mul = grade

    while True:
        if next_mul % 5 == 0:
            break
        next_mul += 1

    if grade < 38:
        print(grade)
    elif (next_mul - grade) < 3:
        print(next_mul)
    elif (next_mul - grade) >= 3:
        print(grade)
