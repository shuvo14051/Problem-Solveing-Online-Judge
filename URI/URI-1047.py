from datetime import datetime, timedelta

h1, m1, h2, m2 = map(int, input().split())

if h1 == h2 and h1 == m1 and h1 == m2:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

else:
    time1 = datetime(2022, 1, 1, h1, m1)
    time2 = datetime(2022, 1, 1, h2, m2)

    time_difference = time2 - time1

    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hours, minutes))