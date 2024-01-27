number, times = map(int, input().split())

for i in range(times):
    if number % 10 == 0:
        number = number // 10
    else:
        number = number -1

print(number)