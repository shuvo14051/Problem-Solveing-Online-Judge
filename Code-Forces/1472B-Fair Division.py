test = int(input())

for _ in range(test):
  
    n = int(input())
    li = list(map(int, input().split()))

    if len(li) % 2 != 0 and sum(li)%2 != 0:
        print("NO")
    elif len(li) % 2 != 0 and sum(li)%2 == 0:
        print("YES")
    elif li.count(1) == li.count(2) and len(li) == 2:
        print("NO")
    elif li.count(1) == li.count(2) and li.count(1)!=1 and li.count(2)!=1:
        print("YES")
    elif len(set(li)) == 1:
        print("YES")