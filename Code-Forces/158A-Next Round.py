n, k = map(int, input().split())
lists = list(map(int, input().split()))[:n]
count = 0

# if len(set(lists)) == 1 and lists[0] > 0:
#     count = n
#     print("this block if")
temp = lists[k-1]
for i in lists:
    if i >= temp and i > 0:
        count += 1    

print(count)