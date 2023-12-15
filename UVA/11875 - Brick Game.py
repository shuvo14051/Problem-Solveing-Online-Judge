test_case = int(input())
for i in range(test_case):
      n = int(input())
      ar = list(map(int,input().split()[:n]))
      ar.sort()
      pop_item = n//2
      for i in range(pop_item):
            ar.pop()
      final_result = ar.pop()
      print(final_result)
