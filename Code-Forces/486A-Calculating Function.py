# n = int(input())
# summ = 0
# for i in range(1, n+1):
#     if i%2 == 0:
#         summ += i
#     else:
#         summ -= i

# print(summ)

n = int(input())

if n % 2 == 0:
     result = n // 2 
else:
     result = -(n // 2 + 1)

print(result)