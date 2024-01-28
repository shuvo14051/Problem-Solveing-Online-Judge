# n = int(input())
# li = list(map(int, input().split()))

# for i in li:
#     if li.count(i) == 1:
#         print(i)


k,arr = int(input()),list(map(int, input().split()))
myset = set(arr)
print(((sum(myset)*k)-(sum(arr)))//(k-1))