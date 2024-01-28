summ = int(input())
li = [5, 4, 3, 2, 1]
count = 0
i = 0

while summ > 0 and i < len(li):
    if summ >= li[i]:
        count += 1
        summ -= li[i]
  
    i += 1

print(count)
