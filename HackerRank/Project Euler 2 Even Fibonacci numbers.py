# Solved
test = int(input())
for i in range(test):
    li = []
    nterms = int(input())
    n1, n2 = 1, 2
    count = 0
    while count < nterms:
        if n1 >= nterms:
            break
        li.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    result = sum([x for x in li if x % 2 == 0])
    print(result)
