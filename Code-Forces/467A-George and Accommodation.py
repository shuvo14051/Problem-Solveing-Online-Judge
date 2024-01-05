n = int(input())

rooms = 0

for i in range(n):
    a, b = map(int, input().split())
    if b-a >= 2:
        rooms += 1
print(rooms)