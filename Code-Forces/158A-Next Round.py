n, k = map(int, input().split())
lists = list(map(int, input().split()))[:n]

result = k
for i in lists[k+1:]:
    # if i == 0:
    #     result = 0
    #     print(i)
    #     break
    if i == lists[k+1]:
        result += 1

print(result)