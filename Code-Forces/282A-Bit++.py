n = int(input())
x = 0
for i in range(n):
    bit = input()
    if bit == '++X' or bit == 'X++':
        x+=1
    elif bit == '--X' or bit == 'X--':
        x-=1

print(x)