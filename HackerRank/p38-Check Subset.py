t = int(input())

def subset(A, B):
    if len(A) >  len(B):
        return False
    else:
        for i in A:
            if i not in B:
                return False
    return True

for i in range(t):
    n = int(input())
    A = set(map(int, input().split()))

    m = int(input())
    B = set(map(int, input().split()))

    result = subset(A, B)
    print(result)


