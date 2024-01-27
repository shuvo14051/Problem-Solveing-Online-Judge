n = int(input())
line = input()[:n]

count = 0
result = 0

for i in line:
    if i == 'D':
        count += 1
    elif i == 'U':
        count -= 1
    if count == 0 and i == "U":
            result += 1
    # print(i, count, result)
    
print(result)