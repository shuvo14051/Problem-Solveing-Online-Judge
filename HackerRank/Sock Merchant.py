n = int(input())
dict = {}
pair = []
final_pair = []
arr = list(map(int, input(). split()[:n]))
for i in arr:
	if i in dict:
		dict[i] += 1
	else:
		dict[i] = 1

for j in dict.values():
	pair.append(j)
	
for k in pair:
	final_pair.append(k//2)
	
print(sum(final_pair))
