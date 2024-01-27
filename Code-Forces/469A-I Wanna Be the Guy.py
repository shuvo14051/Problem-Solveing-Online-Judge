n = int(input())

levels1 = list(map(int, input().split()))
levels2 = list(map(int, input().split()))

final = levels1+levels2

final = set(final)

if len(final) == n:
    print("I become the guy.")

else:
    print("Oh, my keyboard!")