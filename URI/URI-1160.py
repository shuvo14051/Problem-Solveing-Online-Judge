t1 = 0
t2 = 0
count = 0
a = 90000
b = 120000
t1 = t1 + a + int((a*5.5))
t2 = t2 + b + int((b * 3.5))

while t1 != t2:
	t1 += int((a*5.5))
	t2 += int((b*3.5))
	count += 1

print(count)