n = int(input())
left_values = []
enter_values = []
li = []
for i in range(n):
    left, enter = map(int, input().split())
    left_values.append(left)
    enter_values.append(enter)

for j in range(n-1):
    first = enter_values[j] - left_values[j+1] + enter_values[j+1]
    li.append(first)
    li.append()
    print(enter_values[j], left_values[j+1] , enter_values[j+1], enter_values[j] - left_values[j+1] + enter_values[j+1])

# print(max(li))
# print(li)