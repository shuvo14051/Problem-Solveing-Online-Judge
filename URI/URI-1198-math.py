while True:
	try:
		hasmat,opponant = map(int,input().split())
		if(hasmat>opponant):
			diff = hasmat - opponant
		else:
			diff = opponant - hasmat
		print(diff)
	except EOFError:
		break
