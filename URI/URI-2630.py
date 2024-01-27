test = int(input())
count = 1
res = 0
for _ in range(test):
    operation = input()
    li = list(map(int, input().split()))
    if operation == 'min':
        res =  min(li)
    elif operation == 'max':
        res = max(li)
    elif operation == 'mean':
        res =  sum(li)//len(li)
    elif operation == 'eye':
        res =  int(li[0]*.3 + li[1]*.59 + li[2]*.11)
    print("Caso #{}: {}".format(count, res))
    count+=1
    