test = int(input())
base = "Timur"
for _ in range(test):
    n = int(input())
    s = input()[:n]
    for i in s:
        if i not in base:
            val = "NO"
            break
        val = "YES"
    print(val)


