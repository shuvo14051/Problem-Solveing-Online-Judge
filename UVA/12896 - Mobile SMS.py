test = int(input('tEST CASE'))
for i in range(test):
      message = ''
      length = int(input('LENGTH'))
      keys = list(map(int,input('k').split()[:length]))
      values = list(map(int,input('v').split()[:length]))
      dic=dict(zip(keys,values))
      for i in dic.keys():
            
            if i == 1:
                  if dic[i] == 1:
                        message+='.'
                  if dic[i] == 2:
                        message+=','
                  if dic[i] == 3:
                        message+='?'
                  if dic[i] == 4:
                        message+='"'
                        
            if i == 2:
                  if dic[2] == 1:
                        message+='a'
                  if dic[2] == 2:
                        message+='b'
                  if dic[2] == 3:
                        message+='c'
                        
            elif i == 3:
                  if dic[3] == 1:
                        message+='d'
                  if dic[3] == 2:
                        message+='e'
                  elif dic[3] == 3:
                        message+='f'
                        
            if i == 4:
                  if dic[4] == 1:
                        message+='g'
                  if dic[4] == 2:
                        message+='h'
                  if dic[4] == 3:
                        message+='i'

            elif i == 5:
                  if dic[5] == 1:
                        message+='j'
                  if dic[5] == 2:
                        message+='k'
                  if dic[5] == 3:
                        message+='l'


            elif i == 6:
                  if dic[6] == 1:
                        message+='m'
                  if dic[6] == 2:
                        message+='n'
                  if dic[6] == 3:
                        message+='o'

            elif i == 7:
                  if dic[7] == 1:
                        message+='p'
                  if dic[7] == 2:
                        message+='q'
                  if dic[7] == 3:
                        message+='r'
                  if dic[7] == 4:
                        message+='s'

            elif i == 8:
                  if dic[8] == 1:
                        message+='t'
                  if dic[8] == 2:
                        message+='u'
                  if dic[8] == 3:
                        message+='v'

            elif i == 9:
                  if dic[9] == 1:
                        message+='w'
                  if dic[9] == 2:
                        message+='x'
                  if dic[9] == 3:
                        message+='y'
                  if dic[9] == 4:
                        message+='z'

            elif i == 0:
                  if dic[i] == 1:
                        message+=' '


      print(message)
                 
                  
            
