t = int(input())
base_hour, base_minute = 24, 0
for _ in range(t):
    hour, minute = map(int, input().split())
    result = (base_hour - hour)*60 + (base_minute - minute)
    print(result)
