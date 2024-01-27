test_case = int(input())
for k in range(test_case):
	number = int(input())
	answer = (((((number*567)//9)+7492)*235)//47)-498
	sring_of_answer = str(answer)
	list_of_sring = list(sring_of_answer)
	digit_of_tens_column = list_of_sring[-2]
	print(digit_of_tens_column)
	
