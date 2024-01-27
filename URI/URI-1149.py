numbers_str = input()
numbers_list = [int(num) for num in numbers_str.split()]

a = numbers_list[0]
n = [num for num in numbers_list[1:] if num > 0][0]

sum = 0

while n!= 0:
    sum += a
    a += 1
    n -= 1

print(sum)

