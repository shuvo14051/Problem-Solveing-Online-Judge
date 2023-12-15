test_case = int(input())
for i in range(test_case):
      n1,n2 = map(int,input().split())
      for i in range(n1,n2+1):
            c = 0
            for j in range(2,i):
                  if i%j==0:
                        c+=1
                  if c == 0:
                        temp=i
                  print(i)
