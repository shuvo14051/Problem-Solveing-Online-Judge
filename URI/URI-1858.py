n = int(input())
li = list(map(int, input().split()))

index_of_smallest = li.index(min(li))

print(index_of_smallest+1)
