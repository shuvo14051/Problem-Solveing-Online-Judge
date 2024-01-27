summ = int(input())
li = [5,4,3,2,1]
count = 0
for i in li:
    if summ % i == 0:
        count += 1
        summ = summ//i

print(count)