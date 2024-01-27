test = int(input())

for _ in range(test):
    count = 0
    inputs = list(map(int, input().split()))
    n = inputs[0]
    li = inputs[1:]
    average = sum(li) / len(li)
    for item in li:
        if item > average:
            count += 1
    result = count / len(li)
    print("{:.3f}%".format(result*100))


