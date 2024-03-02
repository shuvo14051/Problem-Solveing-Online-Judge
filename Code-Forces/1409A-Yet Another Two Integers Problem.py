t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    if a == b:
        print(0)
    else:
        diff = abs(a - b)
        
        arr = [0] * 11
        answer = 0
        for i in range(10, 0, -1):
            arr[i] = diff // i
            diff -= arr[i] * i
            answer += arr[i]

        print(answer)
