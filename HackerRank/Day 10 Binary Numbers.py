n = int(input())
binary = bin(n)[2:]

max_ones = 0
count = 0
for i in binary:
    if i == "1":
        count += 1
        max_ones = max(max_ones,count)
    else:
        count = 0

print(max_ones)