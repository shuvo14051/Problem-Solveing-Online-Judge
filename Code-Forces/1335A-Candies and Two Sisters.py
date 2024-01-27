# This approach has a large time complexity
# test = int(input())

# for i in range(test):

#     n = int(input())

#     count = 0

#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i + j == n and i > j:
#                 count += 1
#     print(count)

test = int(input())

for _ in range(test):
    n = int(input())

    # Calculate count using a mathematical formula
    count = (n - 1) // 2

    print(count)
