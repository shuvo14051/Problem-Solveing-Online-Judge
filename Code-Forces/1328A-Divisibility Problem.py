n = int(input())

for _ in range(n):
    count = 0
    a, b = map(int, input().split())
    reminder = a%b
    if a%b == 0:
        print("0")
    else:
        print(b-reminder)
    
    