n = (input())
lucky = '47'
count = 0
divisors = []

for i in range(3, int(n)+1):
    if int(n) % i == 0:
        divisors.append(i)

outout = []

for div in divisors:
    count = 0
    for j in str(div):
            if j in lucky:
                count += 1
    if count == len(str(div)):
        outout.append("YES")
    else:
        outout.append("NO")

if "YES" in outout:
     print("YES")
else:
     print("NO")
