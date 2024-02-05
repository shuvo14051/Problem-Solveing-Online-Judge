n = int(input())
li_s = []
appned_item = 0
for i in range(n):
    li = list(map(int, input().split()))
    summ = -1*(li [0]) + li[1] 
    appned_item += summ
    li_s.append(appned_item)

print(max(li_s))
