test_case = int(input())
i = 1
for k in range(test_case):
	li = []
	a,b,c = map(int,input().split())
	li.append(a)
	li.append(b)
	li.append(c)
		#print(li)
	li.sort()
		#print(li)
	li.pop(0)
		#print(li)
	li.pop(-1)
		#print(li)
	result = li[0]
	print ('Case '+str(i)+': '+str(result))
	i+=1

