ar = list(map(int,input().split()[:5]))

result_list = []


for i in range(5):
    sum = 0
    ar_copy = ar[:]
    ar_copy.pop(i)


    for j in ar_copy:
        sum += j
    result_list.append(sum)

maximum = max(result_list)
minimum = min(result_list)
print(minimum, maximum)


