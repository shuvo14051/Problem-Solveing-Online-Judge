test_case = int(input())
for i in range(test_case):
	l,w,h = map(int,input().split())
	if l>20 or w>20 or h>20:
		print('Case '+str(i+1)+': '+ 'bad')
	else:
		print('Case '+str(i+1)+': '+ 'good')
