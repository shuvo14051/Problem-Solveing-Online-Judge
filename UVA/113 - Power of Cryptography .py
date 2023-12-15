try:
	while True:
		n = int(input())
		k = int(input())
		m = 1/n
		ans = pow(k,m)
		ans_int = int(ans)
		if (ans-ans_int) >= .5:
			result = ans_int+1
		else:
			result = ans_int
		print(result)
		
except EOFError:
	pass
# Done