n = int(input())

li = list(map(int, input().split()))[:n]

print(sum(li)/len(li))