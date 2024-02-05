n, m  = map(int, input().split())
count = 0

# check m is prime of not
for i in range(2, m):
    if m%i == 0:
        count += 1 
# also need to check is there any other prime before m
li = list(range(n+1,m))
prime = 0
for num in li:
    c = 0
    for i in range(2, num):
        if num % i == 0 :
            c += 1
    if c == 0:
        prime += 1


if count == 0 and prime == 0:
    print("YES")
else:
    print("NO")