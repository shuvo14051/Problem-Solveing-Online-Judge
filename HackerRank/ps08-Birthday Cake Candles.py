n = int(input())
ar = list(map(int,input().split()[:n]))

tallest = max(ar)

result = ar.count(tallest)

print(result)