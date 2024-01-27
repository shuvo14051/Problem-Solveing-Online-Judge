test = int(input())

def increasing(li):
    for i in range(1, len(li)):
        if li[i-1] >= li[i]:
          return False
    return True


for _ in range(test):
    n = int(input())
    li = list(map(int, input().split()))
    li = sorted(li)
    result = increasing(li)
    if result:
        print("YES")
    else:
        print("NO")


    