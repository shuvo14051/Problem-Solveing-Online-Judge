n = input()
val = 0
for i in n:
    if i == '4' or i == '7':
        val += 1

if val == 4 or val == 7:
    print("YES")
else:
    print("NO")