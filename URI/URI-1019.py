seconds = int(input())

hour = seconds // 3600
remaining_seconds = seconds % 3600

minutes = remaining_seconds // 60
remaining_seconds2 = remaining_seconds % 60

print("%d:%d:%d" % (hour, minutes, remaining_seconds2))
