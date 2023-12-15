import math 
try:
	while True:
		count = 0
		a,b = map(int,input().split())
		if a==0 and b == 0:
			break
		for i in range(a,b+1):
			c = int(math.sqrt(i))
			if c*c == i:
				count+=1
		print(count)
		
except EOFError:
	pass
