n = int(input())
line = list(input().lower())[:n]
unique = set(line)

if len(unique) == 26:
    print("YES")
else:
    print("NO")
