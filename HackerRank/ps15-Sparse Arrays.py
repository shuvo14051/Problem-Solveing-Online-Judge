n = int(input())
string = []
query = []
result = []
for i in range(n):
    s = input()
    string.append(s)

m = int(input())

for j in range(m):
    q = input()
    query.append(q)

for i in query:
    count = 0
    for j in string:
        if i == j:
            count += 1
    result.append(count)

for i in result:
    print(i)