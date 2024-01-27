test_case = int(input())
c = 1
for i in range(test_case):
      n,k,p = map(int,input().split())
      ans = k+p
      while ans>n:
            ans = ans-n
      print('Case '+str(c)+': '+str(ans))
      c+=1
