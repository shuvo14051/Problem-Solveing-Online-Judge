n = int(input())
ar = list(map(int,input().split()[:n]))

positive = 0
negative = 0
zero = 0

for i in ar:
    if i<0:
        negative += 1
    elif i == 0:
        zero += 1
    elif i > 0:
        positive += 1

pos_portion = positive/n
neg_portion = negative/n
zero_portion = zero/n

print("%.6f" %pos_portion)
print("%.6f" %neg_portion)
print("%.6f" %zero_portion)

