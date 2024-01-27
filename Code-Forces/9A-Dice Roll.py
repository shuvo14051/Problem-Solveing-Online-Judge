yw = list(map(int, input().split()))

maxx = max(yw)
count = 0
for i in range(1,7):
    if i >= maxx:
        count += 1

if 6 % count == 0:
    print("{}/{}".format(count//count, 6//count))

elif count % 2 == 0:
    print("{}/{}".format(count//2, 6//2))

else:
    print("{}/{}".format(count, 6))

