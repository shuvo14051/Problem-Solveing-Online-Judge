N = int(input())
data = [int(x) for x in input().split()]

# if the last number ends with 0 only then
# the formed number will be divisible by 10
ele = data[N-1]
if ele % 10 == 0:
    print("Yes")
else:
    print("No")
    
"""
### Run time error ####

N = int(input())
data = [int(x) for x in input().split()]

number = ""
for num in data:
    number += str(num)[-1]

if int(number) % 10 == 0:
    print("Yes")
else:
    print("No")
"""


