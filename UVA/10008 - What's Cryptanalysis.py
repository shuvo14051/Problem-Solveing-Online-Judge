n = int(input())
d = {}
baseline = "abcdefghijklmnopqrstuvwxyz"
for i in range(n):
	m = input().lower()
	for j in m:
		if j in baseline:
			if j not  in d:
				d[j] = 1
			else:
				d[j] += 1
sorted_dict = dict(sorted(d.items(), key=lambda item: (-item[1], item[0])))

for key, value in sorted_dict.items():
    print(key.upper(), value)