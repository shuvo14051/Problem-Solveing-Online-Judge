test = int(input())

for _ in range(test):
    li = list(map(int, input().split()))
    li.remove(max(li))
    print(max(li))