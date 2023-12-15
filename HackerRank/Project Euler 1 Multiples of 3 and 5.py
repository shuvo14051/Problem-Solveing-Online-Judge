#two test case gave time limit
test = int(input())

for i in range(test):
    result = 0
    n = int(input())
    for j in range(2, n):
        if j % 3 == 0 or j % 5 == 0:
            result += j
    print(result)
