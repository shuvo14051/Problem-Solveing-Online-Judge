try:
	while True:
		mir = ''
		data = input()
		if data == '':
			break
		data = data.upper()
		# ~ print(data)
		reverse = data[::-1]
		mirror = 'AEHILJMOSTUVWXYZ123580'
		li = list(data)
		for i in li:
			if i in mirror:
				mir = mir+i
		if mir == data and reverse == data:
			print(data+' -- is a mirrored palindrome.')
			print()
			
		elif mir == data and reverse != data:
			print(data+' -- is a mirrored string.')
			print()
			
		elif mir != data and reverse == data:
			print(data+' -- is a regular palindrome..')
			print()
			
		elif reverse!= data and mir != data:
			print(data+' --  is not a palindrome.')
			print()
except EOFError:
	pass
