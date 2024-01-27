n = int(input())
line = input()[:n]

A = 0
D = 0
for i in line:
    if i == 'D':
        D += 1
    else:
        A += 1

if A == D:
    print("Friendship")
elif A > D:
    print("Anton")
else:
    print("Danik")