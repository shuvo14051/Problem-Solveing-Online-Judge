start, start_min, end, end_min = map(int, input().split())

if start == end:
    hour = 24
elif start > end:
    hour = end + 24 - start
else:
    hour = end-1 - start

if start_min == end_min:
    minute = 0
elif start_min > end_min:
    minute = end_min + 60 - start_min
else:
    minute = end_min - start_min

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hour, minute))