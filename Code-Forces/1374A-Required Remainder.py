# test = int(input())

# for _ in range(test):
#     li = []
#     x, y, n = map(int, input().split())
#     for k in range(n):
#         if k%x == y:
#             li.append(k)
#     print(max(li))

test = int(input())

for _ in range(test):
    x, y, n = map(int, input().split())
    
    # Find the maximum value less than or equal to n with the given condition
    result = (n - y) // x * x + y
    
    print(result)
