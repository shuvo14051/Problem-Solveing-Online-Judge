days = int(input())

years = days // 365
remaining_days = days % 365

days = remaining_days // 30
remaining_days2 = remaining_days % 30

print("%d ano(s)" %years)
print("%d mes(es)" %days)
print("%d dia(s)" %remaining_days2)
