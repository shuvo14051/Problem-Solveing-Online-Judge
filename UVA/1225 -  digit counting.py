test_case = int(input())
for i in range(test_case):
	n,n1,n2,n3,n4,n5,n6,n7,n8,n9 = 0,0,0,0,0,0,0,0,0,0
	string = ''
	number = int(input())
	if(number>20):
		break
	for k in range(1,number+1):
		j = str(k)
		string+=j
	print(string)
	for i in string:
		if i=='0':
			n+=1
		
		if i=='1':
			n1+=1
		
		if i=='2':
			n2+=1
		
		if i=='3':
			n3+=1
		
		if i=='4':
			n4+=1
		
		if i=='5':
			n5+=1
		
		if i=='6':
			n6+=1
		
		if i=='7':
			n7+=1
		
		if i=='8':
			n8+=1
		
		if i=='9':
			n9+=1
	print(n,n1,n2,n3,n4,n5,n6,n7,n8,n9)
	
