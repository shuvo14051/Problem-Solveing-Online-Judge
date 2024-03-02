# test = int(input())

# for _ in range(test):
#     n = int(input())
#     li = list(map(int, input().split()))
#     i = 1
#     while i < len(li):
#         if abs(li[i-1] - li[i]) == 1:
#             minimum = min(li[i], li[i-1])
#             li.remove(minimum)
#         elif li[i-1] == li[i]:
#             li.remove(li[i])
#         else:
#             i += 1

#     if len(li) == 1:
#         print("YES")
#     else:

#         print("NO")
