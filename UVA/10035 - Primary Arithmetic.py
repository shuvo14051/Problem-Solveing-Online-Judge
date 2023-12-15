try:
      while True:
            n1,n2 = map(int,input().split())
            c = 0
            n1 = abs(n1)
            n2 = abs(n2)
            if n1 == 0 and n2 ==0:
                  break
            
            while (n1!=0) and (n2!=0):
                  r1 = n1%10
                  r2 = n2%10
                  if(r1+r2)>9:
                        c+=1
                  n1 = n1//10
                  n2 = n2//10
                  if(r1+r2)>9:
                        n2 = n2+1
                        
            if c == 0:
                  print('No carry operation.')
            else:
                  print(str(c),' carry operation.')

except EOFError:
      pass
