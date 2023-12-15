n = int(input())

a = 0
b = 1
result = ' '
for i in range(n):
    result = result + str(a) + ' '
    # print(a,end=' ')
    # print(result)
    temp = a+b
    a = b
    b = temp

print(result.strip())
