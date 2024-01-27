test_case = int(input())
c = 1
for i in range(test_case):
	a = int(input())
	b = int(input())
	ans = 0
	for i in range(a,b+1):
		if i%2 != 0:
			ans+=i
	print('Case '+str(c)+': '+str(ans))
	c+=1
