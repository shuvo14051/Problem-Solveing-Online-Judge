"""Approach 01 
Time limit exceeded
"""

# test = int(input())

# def sum_of_digits(inp):
#     summ = 0
#     str_inp = str(inp)
#     for i in str_inp:
#         summ += int(i)

#     return summ

# def interesting_number(digit):
#     count = 0
#     if digit <= 8:
#         return 0
#     else:
#         for i in range(10, digit + 1):
#             if sum_of_digits(i) > sum_of_digits(i+1):
#                 count += 1

#     return count

 
"""
The second approach is to count the number of numbers 
that ends with 9
"""
test = int(input())
def count_numbers_ending_with_9(limit):
    count = (limit +1 ) // 10
    return count

for _ in range(test):
    n = int(input())
    res = count_numbers_ending_with_9(n)
    print(res)
    
    
    
    


        
        