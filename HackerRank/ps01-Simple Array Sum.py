n = int(input())
result = 0

arr = list(map(int,input().split()))[:n]

#result = sum(arr) #pythonic way

for i in arr:
    result += i
print(result)