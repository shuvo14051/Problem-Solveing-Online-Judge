number_of_people = 0
total_age = 0
while True:
    age = int(input())
    if age < 0:
        break
    total_age += age
    number_of_people += 1

avg = total_age/number_of_people

print("%.2f" %avg)
