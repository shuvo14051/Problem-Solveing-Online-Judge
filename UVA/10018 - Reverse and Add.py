test_case = int(input())
for i in range(test_case):
	n = input()
	for j in range(1,100):
		n_rev = n[::-1]
		add = int(n)+int(n_rev)
		add_str = str(add)
		add_str_rev = add_str[::-1]
		if add_str == add_str_rev:
			break
		n = add_str
	print(str(j),add_str)
	

