time = input()
h = ''
if time.endswith("PM"):
    hour = time[0:2]

    if hour == '01':
        h = '13'

    elif hour == '02':
        h = '14'

    elif hour == '03':
        h = '15'

    elif hour == '04':
        h = '16'

    elif hour == '05':
        h = '17'

    elif hour == '06':
        h = '18'

    elif hour == '07':
        h = '19'

    elif hour == '08':
        h = '20'

    elif hour == '09':
        h = '21'

    elif hour == '10':
        h = '22'

    elif hour == '11':
        h = '23'

    elif hour == '12':
        h = '12'

    print(h+time[2:8])

elif time.startswith("12") and time.endswith("AM"):
    print('00' + time[2:8])

elif time.endswith("AM"):
    print(time[0:8])
