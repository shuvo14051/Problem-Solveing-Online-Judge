try:
      while True:
            number_of_people = int(input())
            if number_of_people == 0:
                  break
            ages_of_people = list(map(int,input().split()[:number_of_people]))
            ages_of_people.sort()
            for i in ages_of_people:
                  print(i,end = ' ')
except EOFError:
      pass
