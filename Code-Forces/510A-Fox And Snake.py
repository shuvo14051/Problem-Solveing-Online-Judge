a, b = map(int, input().split())

even = '#'*b + '\n'
odd1 = '.'*(b-1) + '#' +'\n'
odd2 = '#' + '.'*(b-1)+'\n'
results = ''

first_odd = 1
second_odd = 3

for i in range(a):
    if i%2 == 0:
        results += even
    elif i%2 == 1 and i%first_odd == 0:
        results += odd1
        first_odd += 4
    elif i%2 ==  1 and i%second_odd == 0:
        results += odd2
        second_odd += 4
        
print(results)