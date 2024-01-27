try:
	while True:
		test_case = int(input())
		
		i = 1
		for k in range(test_case):
			p_day,p_month,p_year =  map(int,input().split())
			b_day,b_month,b_year =  map(int,input().split())
			
	
			if p_day<b_day:
				p_day += 30
				b_month += 1
			day = p_day - b_day
	
			if p_month<b_month:
				p_month += 12
				b_year += 1
			month = p_month - b_month
			year = p_year-b_year
	
			if year >130:
				print ('Case #'+str(i)+': '+'Check birth date')
		
			elif year <0:
				print ('Case #'+str(i)+': '+'Invalid birth date')
		
			else:
				print ('Case #'+str(i)+': '+str(year))
			i+=1
except EOFError:
	pass


