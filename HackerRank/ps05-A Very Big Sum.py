n = int(input())
ar = list(map(int,input().split()[:n]))

sum_of_ar = 0
for i in ar:
    sum_of_ar += i

print(sum_of_ar)