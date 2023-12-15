n = int(input())

ar = list(map(int, input().split()))
total = 0
for i in ar:
    team = i//3
    team = team*3
    total += team

print(total)