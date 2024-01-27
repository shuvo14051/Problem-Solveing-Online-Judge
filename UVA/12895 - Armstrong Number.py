test_case = int(input())
c = 1
for i in range(test_case):
      number = int(input())
      temp = number
      summ = 0
      
      num_str = str(number)
      power = len(num_str)
      
      while temp!=0:
            reminder = temp%10
            temp = temp//10
            summ+=reminder**power
      if summ == number:
            print('Armstrong')
      else:
            print('Not Armstrong')
      
