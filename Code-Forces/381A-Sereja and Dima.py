n = int(input())
li = list(map(int, input().split()))[:n]
first = 0
second = 0

while li:
    maxi_1 = max(li[0], li[-1])
    first += maxi_1
    li.remove(maxi_1)

    # Check if the list is still not empty after removal
    if li:
        maxi_2 = max(li[0], li[-1])
        second += maxi_2
        li.remove(maxi_2)

print(first, second)