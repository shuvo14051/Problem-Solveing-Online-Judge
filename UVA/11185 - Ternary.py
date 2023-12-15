try:
      while True:
            li=[]
            number = int(input())
            if number<0:
                  break
            if number == 0:
                  print(0)
                  continue
            while number!=0:
                  reminder = number%3
                  li.append(reminder)
                  number = number//3
            li.reverse()
            for i in li:
                  print(i,end='')
            print()
except EOFError:
      pass
