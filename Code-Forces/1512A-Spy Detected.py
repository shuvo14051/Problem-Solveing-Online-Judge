test = int(input())

for _ in range(test):
    unique_num = None
    n = int(input())
    li = list(map(int, input().split()))
    for i in li:
        if li.count(i) == 1:
            unique_num = i

    index = li.index(unique_num)
    print(index+1)