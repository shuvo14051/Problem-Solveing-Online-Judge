positive = 0
sum = 0

for i in range(6):
	
	n = input()
	n= float(n)
	if n>0:
		positive += 1
		sum += n
		
average = sum/positive

print("%d valores positivos" %positive)
print("%.1f" %average)
		
		
	