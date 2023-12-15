import fractions as fr
try:
	while True:
		g = 0
		n = int(input())
		if n == 0:
			break
		for i in range(1,n):
			for j in range(i+1,n+1):
				g+= fr.gcd(i,j)
		print(g)
except EOFError:
	pass
