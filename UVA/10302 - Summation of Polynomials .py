try:
	while True:
		add = 0
		n = int(input())
		
		add=(n*n*(n+1)*(n+1))//4;
		print(add)
except EOFError:
	pass

