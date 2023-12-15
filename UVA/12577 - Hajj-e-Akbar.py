try:
	i = 1
	while True:
		inp = input()
		if inp == '*':
			break
		if inp == 'Hajj':
			print ('Case '+str(i)+': '+'Hajj-e-Akbar')
		else:
			print('Case '+str(i)+': '+'Hajj-e-Asghar')
		i = i+1
except EOFError:
	pass

