n = int(input())

ar = list(map(int,input().split()))[:n]
ar2 = ar[:] #copy the list "ar"
winner = max(ar)

#removing all the champions
for i in ar2: #if we user the same list here  the remove operation will not remove all the same items
    if i == winner:
        ar.remove(winner)

runner_up = max(ar)
print(runner_up)