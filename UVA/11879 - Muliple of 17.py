try:
      while True:
            number = int(input())
            if number == 0:
                  break
            reminder = number%10
            number = number//10
            
            five_times_rem = reminder*5
            
            mul = number-five_times_rem
            
            if mul%17 == 0:
                  print(1)
            else:
                  print(0)
except EOFError:
      pass
