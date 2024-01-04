row = int(input())
column = 3
ar = [[0 for _ in range(column)] for _ in range(row)]

for i in range(row):
    row_input = input()
    values = list(map(int, row_input.split()))
    ar[i] = values

number_of_problems = 0

for line in ar:
    count = 0
    for item in line:
        if item > 0:
            count += 1
    if count >= 2:
        number_of_problems += 1
        
print(number_of_problems)
    
    
# This approach gave me a run time error
# n = int(input())

# ar = [[0 for _ in range(3)] for _ in range(n)]

# for i in range(n):
#     for j in range(3):
#         ar[i][j] = int(input())

# number_of_problems = 0

# for line in ar:
#     count = 0
#     for item in line:
#         if item > 0:
#             count += 1
#     if count >= 2:
#         number_of_problems += 1
        
# print(number_of_problems)