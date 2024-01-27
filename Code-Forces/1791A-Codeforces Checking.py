test = int(input())

for _ in range(test):
    base = "codeforces"
    ch = input().lower()
    if ch in base:
        print("YES")
    else:
        print("NO")