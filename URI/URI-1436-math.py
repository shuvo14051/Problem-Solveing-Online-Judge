n = int(input())

for i in range(n):
    li = list(map(int, input().split()))
    sorted_li = sorted(li)
    mid = len(sorted_li) // 2
    print("Case {}: {}".format(i+1, sorted_li[mid]))