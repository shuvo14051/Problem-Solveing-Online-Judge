test_case = int(input())
for i in range(test_case):
	a,b = map(int,input().split())
	if a>b:
		print('>')
	elif a<b:
		print('<')
	else:
		print('=')
