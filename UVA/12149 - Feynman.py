try:
	while True:
		total_squares = 0
		lines = int(input())
		if lines == 0:
			break
		for i in range(1,lines+1):
			total_squares += i*i
		print(total_squares)
		
except EOFError:
	pass
