try:
      while True:
            h1,m1,h2,m2 = map(int,input().split())
            if h1==0 and m1 == 0 and h2 == 0 and m2 == 0:
                  break
            if h2<=h1:
                  h2 += 24
            total_minutes = ((h2-h1)*60)+(m2-m1)
            print(total_minutes)
except EOFError:
      pass
