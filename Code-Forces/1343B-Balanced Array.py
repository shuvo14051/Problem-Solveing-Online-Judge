test = int(input())

for _ in range(test):
    li = []
    even = 2
    odd = 1
    n = int(input())
    div = n//2
    if div % 2 != 0:
        print("NO")
        continue
    else:
        print("YES")
        for i in range(n//2):
            li.append(even)
            even += 2
        for i in range(n//2):
            li.append(odd)
            odd += 2

    li[-1] += sum(li[0:n//2]) - sum(li[n//2:])
    for element in li:
        print(element, end=' ')
    print()