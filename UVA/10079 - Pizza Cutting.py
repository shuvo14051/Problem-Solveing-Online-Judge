try:
	while True:
		lines = int(input())
		if lines<0:
			break
		pieces = ((lines*(lines+1))//2) + 1
		print(pieces)
except EOFError:
	pass
