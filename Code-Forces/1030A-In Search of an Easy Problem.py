n = int(input())

li = list(map(int, input().split()))[:n]

s = sum(li)

if s >0:
    print("HARD")
else:
    print("EASY")